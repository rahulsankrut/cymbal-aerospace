"""Static JS asset for the GraphWorkspace sidecar UI."""

APP_JS = """let network = null;
let nodesDataSet = new vis.DataSet();
let edgesDataSet = new vis.DataSet();
let physicsEnabled = true;
let lastStateHash = "";

function escapeHtml(text) {
    if (!text) return '';
    return text.toString()
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}

function safeUrl(url) {
    if (!url) return '';
    try {
        const parsed = new URL(url);
        if (parsed.protocol === 'http:' || parsed.protocol === 'https:') {
            return parsed.href;
        }
    } catch (e) {
        // Fallback
    }
    return '#';
}

const nodeColorMap = {
    directory: '255, 215, 64', // Yellow
    bug: '255, 82, 82',       // Red
    cl: '224, 64, 251',       // Purple
    file: '55, 148, 255',      // Blue
    code_search: '200, 200, 200' // Grey fallback
};

function createSvgIcon(icon, type) {
    const color = nodeColorMap[type] || '200, 200, 200';
    const svg = `
        <svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" viewBox="0 0 50 50">
            <circle cx="25" cy="25" r="21" fill="rgba(${color}, 0.12)" stroke="rgb(${color})" stroke-width="2"/>
            <text x="25" y="32" font-size="22" text-anchor="middle" font-family="-apple-system, sans-serif">${icon}</text>
        </svg>
    `;
    return 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg);
}

const urlParams = new URLSearchParams(window.location.search);
const conversationId = urlParams.get('conversationId') || 'unknown';

function getEmojiForNode(node_id, node_type) {
    if (node_type === 'directory') return '📁';
    if (node_id.endsWith('.py')) return '🐍';
    if (node_id.endsWith('.md')) return '📝';
    if (node_id.endsWith('BUILD')) return '🛠️';
    if (node_id.includes('cl/')) return '🚀';
    if (node_id.includes('b/')) return '🐛';
    return '📄';
}

async function updateGraphData() {
    try {
        const res = await fetch(`/api/data?conversationId=${conversationId}`);
        if (!res.ok) throw new Error("API request failed");
        const data = await res.json();

        const stateHash = JSON.stringify(data);
        if (stateHash === lastStateHash) {
            document.getElementById('status-message').innerText = `Synced (no changes) | Conv: ${conversationId.substring(0, 8)}`;
            return;
        }
        lastStateHash = stateHash;

        if (!data.nodes || Object.keys(data.nodes).length === 0) {
            document.getElementById('status-message').innerText = "Empty Graph Workspace. Waiting for data...";
            return;
        }

        const visNodes = Object.keys(data.nodes).map(key => {
            const n = data.nodes[key];
            const label = n.node_id.split('/').pop() || n.node_id;
            const type = n.node_type || 'file';
            const emoji = getEmojiForNode(n.node_id, type);
            return {
                id: n.node_id,
                label: label,
                image: createSvgIcon(emoji, type),
                shape: 'image',
                raw: {
                    id: n.node_id,
                    label: label,
                    type: type,
                    icon: emoji,
                    status: n.status || 'closed',
                    path: n.node_id,
                    desc: n.content || 'No content loaded in this turn.'
                }
            };
        });

        const currentNodes = nodesDataSet.getIds();
        const newNodesMap = new Set(visNodes.map(n => n.id));

        currentNodes.forEach(id => {
            if (!newNodesMap.has(id)) nodesDataSet.remove(id);
        });
        nodesDataSet.update(visNodes);

        const visEdges = (data.edges || []).map((e, index) => ({
            id: `e_${e.source_id}_${e.target_id}_${e.relationship_label || ''}`,
            from: e.source_id,
            to: e.target_id,
            label: (e.relationship_label || '').toLowerCase()
        }));

        const currentEdges = edgesDataSet.getIds();
        const newEdgesMap = new Set(visEdges.map(e => e.id));

        currentEdges.forEach(id => {
            if (!newEdgesMap.has(id)) edgesDataSet.remove(id);
        });
        edgesDataSet.update(visEdges);

        document.getElementById('status-message').innerText = `Synced | Conv: ${conversationId.substring(0, 8)}`;
    } catch (err) {
        console.error("updateGraphData caught error:", err);
        if (err.stack) {
            console.error("Error stack:", err.stack);
        }
        document.getElementById('status-message').innerText = `Error: ${err.message}`;
    }
}

document.addEventListener('DOMContentLoaded', function(){
    console.log("DOMContentLoaded handler triggered");
    console.log("Checking window.vis:", typeof window.vis, window.vis);
    console.log("Checking window.goog:", typeof window.goog, window.goog ? Object.keys(window.goog) : null);
    if (window.goog && window.goog.dom) {
        console.log("Checking window.goog.dom:", Object.keys(window.goog.dom));
        if (window.goog.dom.safe) {
            console.log("Checking window.goog.dom.safe:", Object.keys(window.goog.dom.safe));
        }
    }
    document.getElementById('conversation-id-val').innerText = conversationId;
    const container = document.getElementById('mynetwork');
    const data = { nodes: nodesDataSet, edges: edgesDataSet };

    const options = {
        nodes: {
            borderWidth: 0,
            size: 22,
            font: {
                color: '#ffffff',
                size: 11,
                face: '-apple-system, BlinkMacSystemFont, sans-serif',
                vadjust: 30
            }
        },
        edges: {
            width: 1.5,
            color: {
                color: '#444444',
                highlight: '#00e5ff',
                hover: '#666666'
            },
            arrows: {
                to: {
                    enabled: true,
                    scaleFactor: 0.8,
                    type: 'arrow'
                }
            },
            smooth: {
                enabled: true,
                type: 'cubicBezier',
                roundness: 0.4
            },
            font: {
                color: '#aaaaaa',
                size: 8,
                face: 'monospace',
                background: '#1a1a1a',
                strokeWidth: 0
            }
        },
        physics: {
            enabled: true,
            solver: 'forceAtlas2Based',
            forceAtlas2Based: {
                gravitationalConstant: -75,
                centralGravity: 0.015,
                springConstant: 0.06,
                springLength: 90,
                damping: 0.35,
                avoidOverlap: 1
            },
            stabilization: {
                enabled: true,
                iterations: 200,
                updateInterval: 50
            }
        },
        interaction: {
            hover: true,
            tooltipDelay: 3600000
        }
    };

    network = new vis.Network(container, data, options);

    network.on('click', function(properties) {
        const content = document.getElementById('details-content');
        if (properties.nodes.length > 0) {
            const selectedId = properties.nodes[0];
            const selectedNode = nodesDataSet.get(selectedId);
            if (!selectedNode || !selectedNode.raw) return;
            const data = selectedNode.raw;
            let extraFields = '';

            if (data.type === 'file' || data.type === 'directory') {
                extraFields = `
                    <div class="detail-item">
                        <div class="detail-label">Path</div>
                        <div class="detail-value" style="font-family: monospace; font-size: 0.85em; color: #aaa;">${escapeHtml(data.path)}</div>
                    </div>`;
            } else if (data.type === 'bug') {
                extraFields = `
                    <div class="detail-item">
                        <div class="detail-label">URL</div>
                        <div class="detail-value"><a href="${escapeHtml(safeUrl(data.url))}" target="_blank">${escapeHtml(data.url)}</a></div>
                    </div>`;
            } else if (data.type === 'cl') {
                extraFields = `
                    <div class="detail-item">
                        <div class="detail-label">CL Number</div>
                        <div class="detail-value" style="font-family: monospace; color: #e040fb;">${escapeHtml(data.clNum)}</div>
                    </div>`;
            }

            content.innerHTML = `
                <div class="detail-item">
                    <div class="detail-label">ID</div>
                    <div class="detail-value" style="font-family: monospace;">${escapeHtml(data.id)}</div>
                </div>
                <div class="detail-item">
                    <div class="detail-label">Label</div>
                    <div class="detail-value" style="font-weight: bold;">${escapeHtml(data.icon)} ${escapeHtml(data.label)}</div>
                </div>
                <div class="detail-item">
                    <div class="detail-label">Type</div>
                    <div class="detail-value" style="text-transform: capitalize;">${escapeHtml(data.type)}</div>
                </div>
                <div class="detail-item">
                    <div class="detail-label">Status</div>
                    <div class="detail-value">
                        <span class="status-badge status-${escapeHtml(data.status)}">${escapeHtml(data.status.toUpperCase())}</span>
                    </div>
                </div>
                ${extraFields}
                <div class="detail-item">
                    <div class="detail-label">Description</div>
                    <div class="detail-value" style="white-space: pre-wrap; font-family: monospace; font-size: 0.85em; max-height: 200px; overflow-y: auto; background: rgba(0,0,0,0.2); padding: 6px; border-radius: 4px;">${escapeHtml(data.desc)}</div>
                </div>
            `;
        } else if (properties.edges.length > 0) {
            const selectedEdgeId = properties.edges[0];
            const selectedEdge = edgesDataSet.get(selectedEdgeId);
            if (!selectedEdge) return;
            content.innerHTML = `
                <div class="detail-item">
                    <div class="detail-label">Relationship</div>
                    <div class="detail-value" style="font-weight: bold; color: #00e5ff; font-size: 1.1em;">${escapeHtml(selectedEdge.label.toUpperCase())}</div>
                </div>
                <div class="detail-item">
                    <div class="detail-label">Source Node</div>
                    <div class="detail-value" style="font-family: monospace;">${escapeHtml(selectedEdge.from)}</div>
                </div>
                <div class="detail-item">
                    <div class="detail-label">Target Node</div>
                    <div class="detail-value" style="font-family: monospace;">${escapeHtml(selectedEdge.to)}</div>
                </div>
            `;
        } else {
            content.innerHTML = `
                <p style="color: #666; font-style: italic; font-size: 0.9em; text-align: center; margin-top: 40px;">
                    Click on a node or edge to inspect properties.
                </p>
            `;
        }
    });

    updateGraphData();
    setInterval(updateGraphData, 3000);
});

function togglePhysics() {
    if (!network) return;
    physicsEnabled = !physicsEnabled;
    network.setOptions({ physics: { enabled: physicsEnabled } });

    const btn = document.getElementById('toggle-physics-btn');
    if (physicsEnabled) {
        btn.classList.add('active');
        btn.innerText = "Physics: ON";
    } else {
        btn.classList.remove('active');
        btn.innerText = "Physics: OFF";
    }
}

function stabilizeNetwork() {
    if (!network) return;
    network.stabilize();
}
"""
