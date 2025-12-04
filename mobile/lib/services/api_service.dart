import 'dart:convert';
import 'package:http/http.dart' as http;
import '../utils/constants.dart';

class ApiService {

  static Future<String> sendMessage(String msg) async {
    final url = Uri.parse(AppConstants.chatEndpoint);

    final res = await http.post(
      url,
      headers: {"Content-Type": "application/json"},
      body: jsonEncode({"message": msg}),
    );

    final data = jsonDecode(res.body);
    return data["reply"] ?? "Server error";
  }
}
