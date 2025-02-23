- [ ] implementing AI player
- [ ] change `Tank.display` implementation
- [ ] optimize that, seems like we create threads each loop:
    ```python
                while not self.stop_flag.is_set():
                    client_socket, client_address = self.sock.accept()
    
                    thread = threading.Thread(target=self.client_handler, args=(self.init_client(client_socket, client_address),))
                    thread.daemon = True  # Permet d'arrêter les threads lorsqu'ils ne sont plus nécessaires
                    thread.start()
    
                    for th in self.threads:
                        th.start()
    
                    self.threads.append(thread)
    ```