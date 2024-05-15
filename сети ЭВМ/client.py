from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
import socket
import threading


class KovmasApp(App):
    def Hello(self, instance):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

        serv_ip = "127.0.0.1"
        serv_port = 5005
        sock.connect((serv_ip, serv_port))

        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        def lis(sock_UDP):
            while True:
                mass = sock_UDP.recv(1024)
                print('\r' + mass.decode() + "\nYou >>> ", end='')

        threading.Thread(target=lis, args=(sock,), daemon=True).start()

        sock.send('//ready!'.encode())


    def build(self):
        bl = BoxLayout(orientation='vertical', padding=25)
        gl = GridLayout(cols=4, spacing=3, size_hint=(1, .6))

        bl.add_widget(Label(text='Ковмас', font_size=120, size_hint=[1, .4], color='#ff00f7'))

        gl.add_widget(Button(text='Подключиться к серверу', background_color='#9e0099', background_normal='',
                             on_press=self.Hello))
        bl.add_widget(gl)
        return bl


if __name__ == "__main__":
    KovmasApp().run()
