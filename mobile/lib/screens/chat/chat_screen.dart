import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../../controllers/chat_controller.dart';
import '../../components/message_bubble.dart';

class ChatScreen extends StatefulWidget {
  const ChatScreen({super.key});

  @override
  State<ChatScreen> createState() => _ChatScreenState();
}

class _ChatScreenState extends State<ChatScreen> {
  final TextEditingController _controller = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (_) => ChatController(),
      child: Consumer<ChatController>(
        builder: (_, chat, __) {
          return Scaffold(
            appBar: AppBar(
              title: const Text("AvtarX Chat"),
              backgroundColor: Colors.black,
            ),
            body: Column(
              children: [
                Expanded(
                  child: ListView.builder(
                    padding: const EdgeInsets.only(top: 20),
                    itemCount: chat.messages.length,
                    itemBuilder: (_, i) {
                      final msg = chat.messages[i];
                      return MessageBubble(
                        text: msg["text"],
                        isUser: msg["role"] == "user",
                      );
                    },
                  ),
                ),

                if (chat.isTyping)
                  const Padding(
                    padding: EdgeInsets.all(8.0),
                    child: Text("Typing...", style: TextStyle(fontSize: 14)),
                  ),

                Row(
                  children: [
                    Expanded(
                      child: TextField(
                        controller: _controller,
                        decoration: const InputDecoration(
                          hintText: "Message…",
                          contentPadding: EdgeInsets.all(14),
                        ),
                      ),
                    ),
                    IconButton(
                      icon: const Icon(Icons.send),
                      onPressed: () {
                        if (_controller.text.trim().isNotEmpty) {
                          chat.addUserMessage(_controller.text.trim());
                          _controller.clear();
                        }
                      },
                    )
                  ],
                )
              ],
            ),
          );
        },
      ),
    );
  }
}
