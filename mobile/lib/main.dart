import 'package:flutter/material.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  runApp(const BuildSafeApp());
}

class BuildSafeApp extends StatelessWidget {
  const BuildSafeApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: Scaffold(
        body: Center(
          child: Text(
            "AvatarX Build Test OK",
            style: TextStyle(fontSize: 20),
          ),
        ),
      ),
    );
  }
}
