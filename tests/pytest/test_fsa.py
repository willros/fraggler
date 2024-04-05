from fraggler.utils.fsa_file import FsaFile

def test_read_fsa_file():
    fsa = FsaFile(file="../../demo/multiplex.fsa", ladder="LIZ")
    
    assert fsa.ladder == "LIZ"
    