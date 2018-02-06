# ****************************************************************************************************************************************************************************
# * Author		: Johann Laubscher
# * Date		: 2018/01/30
# * Description	: This Python Script reads an EDIFACT Invoice File and converts it to an XML formatted output file
# ****************************************************************************************************************************************************************************

# BEGINNING of MESSAGE Segment
	# Document_Message_Name
	# 		Document_Name_Code
	#		Code_List_identification_Code
	#		Code_List_Responsible_Agency_Code				
	#		Document_name
	# Document_Identifier
	# Message_Function_Code
	# Example - BGM+220::9:DELIVERY+59665+9'
def doBGM(line):
	print ("Segment : BGM")
	print(line)
	
	return;

def doCOM(line):
	print ("Segment : COM")
	print(line)
	return;

def doCNT(line):
	print ("Segment : CNT")
	print(line)
	return;

def doCTA(line):
	print ("Segment : CTA")
	print(line)
	return;

def doDTM(line):
	print ("Segment : DTM")
	print(line)
	return;

def doIMD(line):
	print ("Segment : IMD")
	print(line)
	return;

def doFTX(line):
	print ("Segment : FTX")
	print(line)
	return;

def doLIN(line):
	print ("Segment : LIN")
	print(line)
	return;

def doNAD(line):
	print ("Segment : NAD")
	print(line)
	return;

def doPIA(line):
	print ("Segment : PIA")
	print(line)
	return;

def doQTY(line):
	print ("Segment : QTY")
	print(line)
	return;

def doRFF(line):
	print ("Segment : RFF")
	print(line)
	return;

def doUNA(line):
	print ("Segment : UNA :")
	print(line)
	return;

def doUNB(line):
	print ("Segment : UNB")
	print(line)
	return;

def doUNH(line):
	print ("Segment : UNH")
	print(line)
	return;

def doUNS(line):
	print ("Segment : UNS")
	print(line)
	return;

def doUNT(line):
	print ("Segment : UNT")
	print(line)
	return;

def doUNZ(line):
	print ("Segment : UNZ")
	print(line)
	return;

def segment_names(segment,line):
	switcher = {
		
		"BGM" : doBGM,
		"COM" : doCOM,
		"CNT" : doCNT,
		"CTA" : doCTA,
		"DTM" : doDTM,
		"FTX" : doFTX,
		"IMD" : doIMD,
		"LIN" : doLIN,
		"NAD" : doNAD,
		"PIA" : doPIA,
		"QTY" : doQTY,
		"RFF" : doRFF,
		"UNA" : doUNA,
		"UNB" : doUNB,
		"UNH" : doUNH,
		"UNS" : doUNS,
		"UNT" : doUNT,
		"UNZ" : doUNZ,
	}
	# Get the function name from switcher dictionary
	# Parse each line based on EDIFACT Segment rules
	switcher.get(segment, "Invalid segment")(line)
	
def file_name ():
	# set up the input file path. Not elegant as it will only work on my Mac but we can work on this later. CI an all!
	filepath = "/Users/Johann/Documents/Coding/Python/Input Files/EDIFACT_File.txt"
	print("Read from File : " + filepath)
	return filepath;

def read_file():
	# open the EDIFACT File
	with open(file_name()) as file: 	
		# now read the fileLine by line
	   	for count, line in enumerate(file):
	   		FirstThree = line[0:3]
	   		print ("Input : " + FirstThree) 
	   		# Set Up the Switcher Directory
	   		segment_names(FirstThree,line)
			
def main():
	# read the file so we can parse it
	read_file()


# ****************************************************************************************************************************************************************************
# * Author		: Johann Laubscher
# * Date		: 2018/01/30
# * Description	: This Python Script reads an EDIFACT File and converts it to an XML formatted output file
# ****************************************************************************************************************************************************************************

main()