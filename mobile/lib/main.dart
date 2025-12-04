import 'package:flutter/material.dart';
import 'theme/app_theme.dart';
import 'screens/chat/chat_screen.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  runApp(const AvtarXApp());
}

class AvtarXApp extends StatelessWidget {
  const AvtarXApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "AvtarX (Test Build)",
      debugShowCheckedModeBanner: false,
      theme: AppTheme.lightTheme,
      darkTheme: AppTheme.darkTheme,
      themeMode: ThemeMode.system,
      home: const ChatScreen(),
    );
  }
}
