import 'package:flutter/material.dart';
import 'package:localstorage/localstorage.dart';
import 'package:mpifrontend/screens/farm_details_Screen.dart';
import 'package:mpifrontend/screens/home_Screens.dart';
import 'package:mpifrontend/screens/login_Screens.dart';
import 'package:mpifrontend/screens/register_Screens.dart';
import 'package:mpifrontend/state/farm_state.dart';
import 'package:mpifrontend/state/sensor_state.dart';
import 'package:mpifrontend/state/user_state.dart';
import 'package:provider/provider.dart';
import 'package:mpifrontend/screens/product_registration_screen.dart';
import 'package:mpifrontend/state/product_state.dart';

main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  LocalStorage storage = new LocalStorage('usertoken');
  final Color customGreen = Color(0xFF00692B);
  @override
  Widget build(BuildContext context) {
    return MultiProvider(
        providers: [
          ChangeNotifierProvider(create: (context) => SensorState()),
          ChangeNotifierProvider(create: (context) => FarmState()),
          ChangeNotifierProvider(create: (context) => UserState()),
          ChangeNotifierProvider(
              create: (context) =>
                  ProductState()), // Add the ProductState provider
        ],
        child: MaterialApp(
          debugShowCheckedModeBanner: false,
          // home: HomeScreen(),
          home: FutureBuilder(
              future: storage.ready,
              builder: (BuildContext context, AsyncSnapshot snapshot) {
                if (snapshot.data == null) {
                  return Scaffold(
                    body: Center(
                      child: CircularProgressIndicator(),
                    ),
                  );
                }
                if (storage.getItem('token') == null) {
                  return LoginScreen();
                }
                return HomeScreen();
              }),
          routes: {
            HomeScreen.routeName: (context) => HomeScreen(),
            FarmDetailsScreens.routeName: (context) => FarmDetailsScreens(),
            LoginScreen.routeName: (context) => LoginScreen(),
            RegisterScreen.routeName: (context) => RegisterScreen(),
            ProductRegistrationScreen.routeName: (context) =>
                ProductRegistrationScreen(), // Add the route for ProductRegistrationScreen
          },
          title: 'MPI',
          theme: ThemeData(
            primarySwatch: MaterialColor(
              customGreen.value,
              <int, Color>{
                50: customGreen,
                100: customGreen,
                200: customGreen,
                300: customGreen,
                400: customGreen,
                500: customGreen,
                600: customGreen,
                700: customGreen,
                800: customGreen,
                900: customGreen,
              },
            ),
          ),
        ));
  }
}
