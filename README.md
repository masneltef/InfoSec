# TLS Handshake Simulation

A simplified simulation of the TLS (Transport Layer Security) handshake process, demonstrating protocol version negotiation, cipher suite selection, and basic Diffie-Hellman key exchange.

## Requirements

- Python 3.x

## Setup

1. Clone or download the project:
   ```
   git clone https://github.com/masneltef/Homework2-tls-handshake.git
   cd tls-handshake-simulation/Homework2_TLS_Handshake
   ```

2. (Optional) Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies (if any):
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the simulation:
```
python src/main.py
```

Follow the on-screen prompts to set TLS versions, cipher suites, and perform the handshake.

## Running Tests

Execute the test suite:
```
python -m unittest discover tests
```

## Project Structure

```
Homework2_TLS_Handshake/
├── src/
│   ├── main.py
│   └── tls_handshake/
│       ├── __init__.py
│       ├── version_negotiation.py
│       ├── cipher_suite_selection.py
│       ├── key_exchange.py
│       └── utils.py
├── tests/
│   ├── test_version_negotiation.py
│   ├── test_cipher_suite_selection.py
│   └── test_key_exchange.py
├── README.md
└── requirements.txt
```

## Author
Yvan Tefiang
