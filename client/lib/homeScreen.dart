import 'package:flutter/material.dart';
import 'communicator.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key, required this.title});

  final String title;

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}


class _HomeScreenState extends State<HomeScreen> {
  final TextEditingController _controller = TextEditingController();
  String _responseText = '';

  void handleResponse(String response) {
    setState(() {
      _responseText = response;
    });
  }

  void initState() {
    super.initState();
    Communicator.getInstance(handleResponse: handleResponse);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            ElevatedButton(
              onPressed: () {
                Communicator.getInstance(handleResponse: handleResponse).send('on');
              },
              child: Text('On'),
            ),
            ElevatedButton(
              onPressed: () {
                Communicator.getInstance(handleResponse: handleResponse).send('off');
              },
              child: Text('Off'),
            ),
            ElevatedButton(
              onPressed: () {
                Communicator.getInstance(handleResponse: handleResponse).send('toggle');},
              child: Text('Toggle'),
            ),
            ElevatedButton(
              onPressed: () {
                Communicator.getInstance(handleResponse: handleResponse).send('blink');},
              child: Text('Blink'),
            ),
          ],
        ),
      ),
    );
  }
}