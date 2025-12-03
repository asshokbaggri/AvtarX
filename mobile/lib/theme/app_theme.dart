import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class AppTheme {
  static ThemeData darkTheme = ThemeData(
    brightness: Brightness.dark,
    scaffoldBackgroundColor: const Color(0xFF0B0E14),
    primaryColor: const Color(0xFF4B7BFF),
    textTheme: TextTheme(
      bodyMedium: GoogleFonts.inter(color: Colors.white),
      headlineSmall: GoogleFonts.poppins(color: Colors.white),
    ),
    fontFamily: GoogleFonts.inter().fontFamily,
    useMaterial3: true,
  );
}
