import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="A bit Racey",
    options={"build_exe": {"packages":["pytube"]}},
    executables = executables

    )


#python setup.py build (command)