import 'package:flutter/material.dart';
import '../services/api_service.dart';

class ChatController extends ChangeNotifier {
  final List<Map<String, dynamic>> messages = [];
  bool isTyping = false;

  void addUserMessage(String text) {
    messages.add({"role": "user", "text": text});
    notifyListeners();
    sendToBackend(text);
  }

  Future<void> sendToBackend(String text) async {
    isTyping = true;
    notifyListeners();

    final reply = await ApiService.sendMessage(text);

    messages.add({"role": "assistant", "text": reply});
    isTyping = false;
    notifyListeners();
  }
}
