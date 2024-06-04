import 'dart:io';

class Communicator {
  Socket? _socket;
  static Communicator? _instance;
  String? responseText;
  Function(String) handleResponse;

  static Communicator getInstance({required Function(String) handleResponse}) {
    _instance ??= Communicator(handleResponse: handleResponse);
    if (_instance?.handleResponse != handleResponse) {
      _instance?.handleResponse = handleResponse;
    }
    return _instance!;
  }

  static void updateHandleResponse(Function(String) handleResponse) {
    _instance?.handleResponse = handleResponse;
  }

  Communicator({required this.handleResponse}) {
    connect();
  }

  void connect() async {
    print('Connecting to server...');
    try {
      _socket = await Socket.connect('192.168.1.13', 65435);
      if (_socket == null) {
        print('Error: Could not connect to server.');
        return;
      } else {
        print('Connected to server.');
      }
    } catch (e) {
      print('Error: $e');
      return;
    }
    _socket?.listen((List<int> event) {
      try {
        String message = String.fromCharCodes(event);
        print("from server: $message");
      } catch (e) {
        print("An error occurred: $e");
      }
    }); 
  }

  void send(String message) {
    if (_socket == null) {
      print('Error: Not connected to server.');
      return;
    }
    _socket!.write(message);
  }
}