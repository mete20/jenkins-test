# test_hello.py
import hello

def test_main(capsys):
    hello.main()
    captured = capsys.readouterr()
    assert captured.out == "Hello, Jenkins!\n"
