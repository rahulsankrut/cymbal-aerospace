import {type ReactNode, useEffect, useState} from 'react';
import './hand-drawn.css';
import {IconDefs} from './IconDefs';

interface Message {
  id: string;
  sender: 'user' | 'assistant';
  text?: string;
  component?: ReactNode;
  canvasLauncher?: {
    url: string;
    name: string;
    icon?: string;
  };
}

/** A2UI Chat Component wrapper for hand-drawn prototyping */
export function HandDrawnChat() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [activeCanvas, setActiveCanvas] = useState<{
    url: string;
    name: string;
    icon?: string;
  } | null>(null);

  // Listen for OPEN_CANVAS postMessage events from inline sandboxes or canvas launchers
  useEffect(() => {
    const handleMessage = (event: MessageEvent) => {
      if (event.data?.type === 'OPEN_CANVAS' && event.data?.payload) {
        setActiveCanvas(event.data.payload);
      }
    };
    window.addEventListener('message', handleMessage);
    return () => window.removeEventListener('message', handleMessage);
  }, []);

  // Auto-open active canvas if the latest assistant message contains a canvas launcher
  useEffect(() => {
    const lastMessage = messages[messages.length - 1];
    if (lastMessage?.sender === 'assistant' && lastMessage.canvasLauncher) {
      setActiveCanvas(lastMessage.canvasLauncher);
    }
  }, [messages]);

  const handleSend = (textToSend?: string) => {
    const query = textToSend || input;
    if (!query.trim()) return;

    const userMsg: Message = {
      id: Date.now().toString(),
      sender: 'user',
      text: query,
    };
    setMessages((prev) => [...prev, userMsg]);
    if (!textToSend) setInput('');

    // Simulate AI responses for demo prompts
    setTimeout(() => {
      if (query.toLowerCase().includes('kitten')) {
        const assistantMsg: Message = {
          id: (Date.now() + 1).toString(),
          sender: 'assistant',
          text: 'I found 3 great adoptable kittens near you!',
          canvasLauncher: {
            url: 'about:blank',
            name: 'Kittens Near You',
            icon: 'pets',
          },
        };
        setMessages((prev) => [...prev, assistantMsg]);
      } else if (query.toLowerCase().includes('pizza')) {
        const assistantMsg: Message = {
          id: (Date.now() + 1).toString(),
          sender: 'assistant',
          text: 'I found 3 great pizza places near you!',
          component: (
            <div
              className="sketchy-box-flat bg-white text-[#202124] p-4 flex flex-col gap-3"
              style={{
                fontFamily: "'Architects Daughter', cursive, sans-serif",
              }}>
              <div className="flex items-center gap-2 border-b border-dashed border-gray-300 pb-2">
                <span className="material-symbols-outlined text-amber-600">
                  local_pizza
                </span>
                <span className=" text-lg">Pizza Near You</span>
              </div>
              <div className="flex flex-col gap-2">
                <div
                  className="p-3 rounded-xl bg-white border border-gray-200 flex justify-between items-center cursor-pointer hover:bg-gray-50"
                  onClick={() =>
                    window.postMessage(
                      {
                        type: 'OPEN_CANVAS',
                        payload: {
                          url: 'pizza-details',
                          name: 'Pizzeria Details',
                          icon: 'store',
                        },
                      },
                      '*',
                    )
                  }>
                  <div>
                    <div className=" text-sm">Luigi's Pizzeria</div>
                    <div className="text-xs text-gray-500">
                      0.4 miles away • ⭐ 4.8
                    </div>
                  </div>
                  <span className="material-symbols-outlined text-gray-400">
                    chevron_right
                  </span>
                </div>
                <div
                  className="p-3 rounded-xl bg-white border border-gray-200 flex justify-between items-center cursor-pointer hover:bg-gray-50"
                  onClick={() =>
                    window.postMessage(
                      {
                        type: 'OPEN_CANVAS',
                        payload: {
                          url: 'pizza-details',
                          name: 'Pizzeria Details',
                          icon: 'store',
                        },
                      },
                      '*',
                    )
                  }>
                  <div>
                    <div className=" text-sm">Slice of Heaven</div>
                    <div className="text-xs text-gray-500">
                      1.2 miles away • ⭐ 4.5
                    </div>
                  </div>
                  <span className="material-symbols-outlined text-gray-400">
                    chevron_right
                  </span>
                </div>
              </div>
            </div>
          ),
        };
        setMessages((prev) => [...prev, assistantMsg]);
      } else {
        const assistantMsg: Message = {
          id: (Date.now() + 1).toString(),
          sender: 'assistant',
          text: `I received your request: "${query}". Try asking for "kittens" or "pizza"!`,
        };
        setMessages((prev) => [...prev, assistantMsg]);
      }
    }, 600);
  };

  return (
    <div
      className="absolute inset-0 flex h-full w-full bg-[#F8F9FA] overflow-hidden"
      style={{fontFamily: "'Architects Daughter', cursive, sans-serif"}}>
      <IconDefs />
      {/* Main Chat Content Area */}
      <div className="flex-1 flex flex-col min-w-0 h-full">
        {/* Top Header */}
        <div className="h-[60px] px-6 bg-[#F8F9FA] border-b border-gray-200 flex items-center justify-between shrink-0">
          <div className="flex items-center gap-2">
            <span className="text-xl ">Hand-drawn chat</span>
          </div>
          <button
            onClick={() => {
              setMessages([]);
              setActiveCanvas(null);
            }}
            className="sketchy-btn bg-white hover:bg-gray-100 text-gray-600 text-sm py-1 px-4">
            Clear chat
          </button>
        </div>

        {/* Message Stream */}
        <div className="flex-1 overflow-y-auto p-6 flex flex-col gap-4 max-w-[800px] w-full mx-auto">
          {messages.map((msg) => (
            <div
              key={msg.id}
              className={`flex flex-col gap-1 w-full ${msg.sender === 'user' ? 'items-end' : 'items-start'}`}>
              {msg.text && (
                <div
                  className={`p-4 rounded-2xl max-w-[85%] text-base ${
                    msg.sender === 'user'
                      ? 'bg-[#DDE7FF] text-[#002D62] rounded-br-none'
                      : 'bg-white border border-gray-200 text-[#202124] rounded-bl-none'
                  }`}>
                  {msg.text}
                </div>
              )}

              {/* Inline Generative UI Widget */}
              {msg.component && (
                <div className="w-full max-w-[420px] mt-2">{msg.component}</div>
              )}

              {/* Canvas Launcher Pill */}
              {msg.canvasLauncher && (
                <div className="sketchy-box-pill w-full bg-white p-3 px-4 flex items-center justify-between gap-4 mt-2 border border-gray-200">
                  <div className="flex items-center gap-2">
                    {msg.canvasLauncher.icon && (
                      <span className="material-symbols-outlined text-purple-600">
                        {msg.canvasLauncher.icon}
                      </span>
                    )}
                    <span className="text-sm ">{msg.canvasLauncher.name}</span>
                  </div>
                  <button
                    onClick={() => setActiveCanvas(msg.canvasLauncher!)}
                    className="sketchy-btn bg-[#F1F3F4] text-xs py-1 px-3 hover:bg-gray-200">
                    {activeCanvas?.url === msg.canvasLauncher.url
                      ? 'Viewing'
                      : 'Open'}
                  </button>
                </div>
              )}
            </div>
          ))}
        </div>

        {/* Prompt Suggestions & Input Bar */}
        <div className="p-4 bg-[#F8F9FA] max-w-[800px] w-full mx-auto shrink-0 flex flex-col gap-2">
          <form
            onSubmit={(e) => {
              e.preventDefault();
              handleSend();
            }}
            className="flex gap-2">
            <div className="flex-1 p-3 px-4 sketchy-box-pill bg-white flex items-center">
              <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder="Enter your prompt"
                className="w-full border-0 outline-none bg-transparent text-base text-[#202124]"
              />
            </div>
            <button
              type="submit"
              className="sketchy-btn bg-[#DDE7FF] text-[#002D62]  px-5 flex items-center justify-center">
              Send
            </button>
          </form>
        </div>
      </div>

      {/* Right-Hand Sliding Canvas Panel */}
      {activeCanvas && (
        <div className="w-[360px] h-full bg-[#F8F9FA] border-l border-gray-200 flex flex-col shrink-0 shadow-lg z-20 relative">
          <div className="absolute top-2 right-2 z-50">
            <button
              onClick={() => setActiveCanvas(null)}
              className="w-10 h-10 rounded-full hover:bg-gray-200 flex items-center justify-center text-gray-500 cursor-pointer">
              <span className="material-symbols-outlined text-xl">close</span>
            </button>
          </div>

          <div className="flex-1 p-4 pt-14 overflow-y-auto">
            <div className="sketchy-box-flat p-4 bg-white border border-gray-200 flex flex-col gap-3">
              <div className=" text-lg border-b border-dashed border-gray-300 pb-2">
                🐾 Adoptable Kittens
              </div>
              <div className="flex flex-col gap-2 text-sm">
                <div className="p-3 rounded-xl bg-white border border-gray-200 flex justify-between items-center cursor-pointer hover:bg-gray-50">
                  <div>
                    <div className="">Mittens</div>
                    <div className="text-xs text-gray-500">
                      2 months • 0.5 miles away
                    </div>
                  </div>
                  <span className="material-symbols-outlined text-gray-400">
                    chevron_right
                  </span>
                </div>
                <div className="p-3 rounded-xl bg-white border border-gray-200 flex justify-between items-center cursor-pointer hover:bg-gray-50">
                  <div>
                    <div className="">Oreo</div>
                    <div className="text-xs text-gray-500">
                      4 months • 1.2 miles away
                    </div>
                  </div>
                  <span className="material-symbols-outlined text-gray-400">
                    chevron_right
                  </span>
                </div>
                <div className="p-3 rounded-xl bg-white border border-gray-200 flex justify-between items-center cursor-pointer hover:bg-gray-50">
                  <div>
                    <div className="">Luna</div>
                    <div className="text-xs text-gray-500">
                      3 weeks • 2.5 miles away
                    </div>
                  </div>
                  <span className="material-symbols-outlined text-gray-400">
                    chevron_right
                  </span>
                </div>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
