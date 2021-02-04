import argparse

argparser = argparse.ArgumentParser(
	description="a foo that bars",
    #formatter_class=argparse.RawTextHelpFormatter,
	epilog="""ant that's how you'd foo a 
           bar""")
print(argparser.print_help())