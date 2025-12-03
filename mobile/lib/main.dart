import 'package:flutter/material.dart';
import 'theme/app_theme.dart';
import 'screens/onboarding/onboarding_screen.dart';

void main() {
  runApp(const AvtarX());
}

class AvtarX extends StatelessWidget {
  const AvtarX({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: "AvtarX",
      theme: AppTheme.darkTheme,
      home: const OnboardingScreen(),
    );
  }
}
