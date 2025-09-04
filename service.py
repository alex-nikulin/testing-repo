from flask import Flask

service = Flask(__name__)

@service.route('/')
def home():
    return 'Hello, Flask!'

def main():
    service.run(debug=True)

if __name__ == '__main__':
    main()