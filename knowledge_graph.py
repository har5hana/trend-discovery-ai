from pyvis.network import Network

net = Network(height="750px", width="100%", bgcolor="#111111", font_color="white")

# Nodes
net.add_node("OpenAI")
net.add_node("GPT")
net.add_node("AI Agents")
net.add_node("MCP")

net.add_node("Google")
net.add_node("Gemini")
net.add_node("Veo")

# Edges
net.add_edge("OpenAI", "GPT")
net.add_edge("OpenAI", "AI Agents")
net.add_edge("OpenAI", "MCP")

net.add_edge("Google", "Gemini")
net.add_edge("Google", "Veo")

# Save graph
net.save_graph("knowledge_graph.html")

print("Graph created!")