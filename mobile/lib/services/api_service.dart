import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  static const String baseUrl = "https://YOUR_RENDER_BACKEND_URL"; // <- CHANGE

  static Future<String> sendMessage(String msg) async {
    final url = Uri.parse("$baseUrl/chat/message");

    final res = await http.post(
      url,
      headers: {"Content-Type": "application/json"},
      body: jsonEncode({"message": msg}),
    );

    final data = jsonDecode(res.body);

    return data["reply"] ?? "Server error";
  }
}
