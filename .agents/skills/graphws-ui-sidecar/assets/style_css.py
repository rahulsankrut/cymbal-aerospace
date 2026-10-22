"""Static CSS asset for the GraphWorkspace sidecar UI."""

STYLE_CSS = """body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    background-color: var(--vscode-editor-background, #1e1e1e);
    color: var(--vscode-foreground, #ccc);
    margin: 0;
    padding: 0;
    display: flex;
    height: 100vh;
    overflow: hidden;
}
#network-container {
    flex-grow: 1;
    height: 100%;
    position: relative;
}
#mynetwork {
    width: 100%;
    height: 100%;
    background-color: #1a1a1a;
    background-image: 
        radial-gradient(rgba(255, 255, 255, 0.04) 1.5px, transparent 0),
        radial-gradient(rgba(255, 255, 255, 0.04) 1.5px, transparent 0);
    background-size: 24px 24px;
    background-position: 0 0, 12px 12px;
}
#toolbar {
    display: flex;
    gap: 8px;
    padding-bottom: 15px;
    border-bottom: 1px solid var(--vscode-widget-border, #3c3c3c);
}
#toolbar button {
    flex: 1;
    background: var(--vscode-button-secondaryBackground, #3a3d41);
    color: var(--vscode-button-secondaryForeground, #ffffff);
    border: none;
    padding: 6px 10px;
    font-size: 11px;
    border-radius: 4px;
    cursor: pointer;
    font-weight: 500;
    transition: all 0.15s ease;
    text-align: center;
}
#toolbar button:hover {
    background: var(--vscode-button-hoverBackground, #4c5055);
}
#toolbar button.active {
    background: var(--vscode-button-background, #3794ff);
    color: var(--vscode-button-foreground, #ffffff);
}
#details-panel {
    width: 280px;
    border-left: 1px solid var(--vscode-widget-border, #3c3c3c);
    background-color: var(--vscode-sideBar-background, #252526);
    padding: 20px;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    gap: 15px;
    overflow-y: auto;
    box-shadow: -4px 0 16px rgba(0, 0, 0, 0.2);
}
h2 {
    color: var(--vscode-sideBarTitle-foreground, #3794ff);
    margin-top: 0;
    margin-bottom: 5px;
    font-size: 1.15em;
    letter-spacing: 0.5px;
}
#conversation-info {
    font-size: 10px;
    color: var(--vscode-descriptionForeground, #858585);
    margin-bottom: 12px;
    font-family: monospace;
    word-break: break-all;
}
.detail-item {
    margin-bottom: 10px;
    animation: fadeIn 0.2s ease;
}
.detail-label {
    font-weight: 600;
    font-size: 0.75em;
    text-transform: uppercase;
    color: #858585;
    letter-spacing: 0.5px;
}
.detail-value {
    margin-top: 4px;
    font-size: 0.9em;
    line-height: 1.4em;
    word-break: break-all;
}
.detail-value a {
    color: #3794ff;
    text-decoration: none;
}
.detail-value a:hover {
    text-decoration: underline;
}
.status-badge {
    display: inline-block;
    padding: 3px 8px;
    border-radius: 12px;
    font-size: 0.75em;
    font-weight: 600;
    letter-spacing: 0.5px;
}
.status-open {
    background-color: rgba(76, 175, 80, 0.15);
    color: #4caf50;
    border: 1px solid rgba(76, 175, 80, 0.3);
}
.status-closed {
    background-color: rgba(158, 158, 158, 0.12);
    color: #9e9e9e;
    border: 1px solid rgba(158, 158, 158, 0.25);
}
#status-message {
    position: absolute;
    bottom: 15px;
    left: 15px;
    z-index: 10000;
    font-size: 10px;
    color: #777;
    background: rgba(20, 20, 20, 0.6);
    padding: 4px 8px;
    border-radius: 4px;
}
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(4px); }
    to { opacity: 1; transform: translateY(0); }
}
"""
