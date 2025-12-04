import 'package:flutter/material.dart';

class AppTheme {
  // COLORS SAME AS CHATGPT
  static const Color primary = Color(0xFF10A37F);
  static const Color background = Color(0xFFF7F7F8);
  static const Color darkBackground = Color(0xFF050509);
  static const Color userBubble = Color(0xFFECECF1);
  static const Color aiBubble = Colors.white;

  static ThemeData lightTheme = ThemeData(
    brightness: Brightness.light,
    scaffoldBackgroundColor: background,
    primaryColor: primary,
    fontFamily: "Inter",
    appBarTheme: const AppBarTheme(
      elevation: 0,
      backgroundColor: background,
      foregroundColor: Colors.black,
    ),
    inputDecorationTheme: InputDecorationTheme(
      border: OutlineInputBorder(
        borderRadius: BorderRadius.circular(14),
        borderSide: const BorderSide(color: Colors.black12),
      ),
    ),
  );

  static ThemeData darkTheme = ThemeData(
    brightness: Brightness.dark,
    scaffoldBackgroundColor: darkBackground,
    primaryColor: primary,
    fontFamily: "Inter",
    appBarTheme: const AppBarTheme(
      elevation: 0,
      backgroundColor: darkBackground,
      foregroundColor: Colors.white,
    ),
  );
}
