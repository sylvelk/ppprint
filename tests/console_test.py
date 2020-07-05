from ppprint import console


def test_console():
    console.log("Hello World !")
    console.warn("Careful ...")
    console.error("Ooops something went wrong !")
    console.info("Climate change is real.")
    console.debug("this code works")
    for i in range(100000):
        console.log("Oh look, a counter : {}".format(i), True)
