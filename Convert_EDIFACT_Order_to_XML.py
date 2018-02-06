# ****************************************************************************************************************************************************************************
# * Author		: Johann Laubscher
# * Date		: 2018/01/30
# * Description	: This Python Script reads an EDIFACT Order File and converts it to an XML formatted output file
# ****************************************************************************************************************************************************************************


def doUNA(line,output_file):
# This line just shows the delimeters used in the EDIFACT File. We don't really need this in 
# the XML file, so do nothing for now
	
	print ("***************************************************************************************************************************************")
	print ("Line 					: " + line)
	print ("***************************************************************************************************************************************")
	print(" ")
	return;



def doUNB(line,output_file):
#
# This is the Message Interchange Header segment.
#
# An example of this segment is as follows:
# UNB+UNOC:3+0041498000042:14+5412345678908:14+150323:1715+12345552+++++EANCOM+1
# 
# The field layout of this segment is as follows:
# Syntax Identifier
#		Syntax Identifier
#		Syntax Version Number
# Interchange Sender
#		Sender Identification
# 		Partner Identification Code Qualifier
# Interchange Recipient
# 		Recipient Identification
#		Recipient Identification Code Qualifier
# Preparation Date and Time
#		Preparation Date
# 		Preparation Time
# Interchange Control Reference
# Recipient's Reference Password
# Application Reference
# Processing Priority Code
# Acknowledgement Request
# Communications Agreement ID
# Test Indicator
#
# Get rid of the last 2 characters on the line 
#
	line = line[:-2]
#	
# Splitting the fields
#
	split_list = line.split("+")
	segment_identifier            = split_list[0]
	syntax_identifier             = split_list[1]
#
	split_sub				      = syntax_identifier.split(":")
	syntax_id                     = split_sub[0]
	syntax_version_number         = split_sub[1]
#	
	interchange_sender            = split_list[2]
	split_sub				      = interchange_sender.split(":")
	sender_id			          = split_sub[0]
	partner_id_code  		      = split_sub[1]
#
	interchange_recipient         = split_list[3]
	split_sub				      = interchange_recipient.split(":")
	recipient_id		          = split_sub[0]
	recipient_id_code  		      = split_sub[1]
#
	preparation_date_time         = split_list[4]
	split_sub				      = preparation_date_time.split(":")
	preparation_date	          = split_sub[0]
	preparation_time  		      = split_sub[1]
#
	interchange_control_reference = split_list[5]
#
	recipient_reference_password  = split_list[6]
#
	application_reference         = split_list[7]
#
	processing_priority_code      = split_list[8]
#
	acknowledgement_request       = split_list[9]
#
	communications_agreement_id	  = split_list[10]
#
	test_indicator                = split_list[11]
	
#	
# Write the XML Structure to the file
#
	output_file.write("	<" + segment_identifier + ">\r\n")
	output_file.write("		<SyntaxIdentifier> \r\n")
	output_file.write("			<SyntaxID>" + syntax_id + "</SyntaxID> \r\n")
	output_file.write("			<SyntaxVersionNumber>" + syntax_version_number  + "</SyntaxVersionNumber> \r\n")
	output_file.write("		</SyntaxIdentifier> \r\n")
	output_file.write("		<InterchangeSender> \r\n")
	output_file.write("			<SenderID>" + sender_id + "</SenderID> \r\n")
	output_file.write("			<PartnerIDCode>" + partner_id_code + "</PartnerIDCode> \r\n")
	output_file.write("		</InterchangeSender> \r\n")
	output_file.write("		<InterchangeRecipient> \r\n")
	output_file.write("			<RecipientID>" + recipient_id + "</RecipientID> \r\n")
	output_file.write("			<RecipientIDCode>" + recipient_id_code + "</RecipientIDCode> \r\n")
	output_file.write("		</InterchangeRecipient> \r\n")
	output_file.write("		<PreparationDateTime> \r\n")
	output_file.write("			<PreparationDate>" + preparation_date + "</PreparationDate> \r\n")
	output_file.write("			<PreparationTime>" + preparation_time + "</PreparationTime> \r\n")	
	output_file.write("		</PreparationDateTime> \r\n")
	output_file.write("		<InterchangeControlReference>" + interchange_control_reference + "</InterchangeControlReference> \r\n")
	output_file.write("		<RecipientReferencePassword>" + recipient_reference_password + "</RecipientReferencePassword> \r\n")
	output_file.write("		<ApplicationReference>" + application_reference + "</ApplicationReference> \r\n")
	output_file.write("		<ProcessingPriorityCode>" + processing_priority_code + "</ProcessingPriorityCode> \r\n")	
	output_file.write("		<AcknowledgementRequest>" + acknowledgement_request + "</AcknowledgementRequest> \r\n")	
	output_file.write("		<CommunicationsAgreementID>" + communications_agreement_id + "</CommunicationsAgreementID> \r\n")	
	output_file.write("		<TestIndicator>" + test_indicator  + "</TestIndicator> \r\n")		
	output_file.write("	</" + segment_identifier + ">\r\n")
	return;
#
def doUNH(line,output_file):
#
# This is the Message Header segment.
#
# An example of this segment is as follows:
# UNH+54322+ORDERS:D:01B:UN:EAN010
# 
# The field layout of this segment is as follows:
# Message Reference Number
# Message Identifier
#	Message Type
#	Message Version Number
#	Message Release Number
#	Controlling Agency
# 	Association Assigned Code
# 
# Get rid of the last 2 characters on the line 
#
	line = line[:-2]
#	
# Splitting the fields
#
	split_list = line.split("+")
	segment_identifier				= split_list[0]
#	
	message_reference_number		= split_list[1]
#
	message_identifier				= split_list[2]	
	split_sub						= message_identifier.split(":")
	message_type					= split_sub[0]
	message_version_number			= split_sub[1]
	message_release_number			= split_sub[2]
	controlling_agency				= split_sub[3]
	association_assigned_code		= split_sub[4]
#	
# Write the XML Structure to the file
#	
	output_file.write("	<" + segment_identifier + ">\r\n")
	output_file.write("		<MessageReferenceNumber>" + message_reference_number + "</MessageReferenceNumber> \r\n")
	output_file.write("		<MessageIdentifier> \r\n")
	output_file.write("			<MessageType>" + message_type + "</MessageType> \r\n")
	output_file.write("			<MessageVersionNumber>" + message_version_number + "</MessageVersionNumber> \r\n")
	output_file.write("			<MessageReleaseNumber>" + message_release_number + "</MessageReleaseNumber> \r\n")
	output_file.write("			<ControllingAgency>" + controlling_agency + "</ControllingAgency> \r\n")
	output_file.write("			<AssociationAssignedCode>" + association_assigned_code + "</AssociationAssignedCode> \r\n")
	output_file.write("		</MessageIdentifier> \r\n")
	output_file.write("	</" + segment_identifier + ">\r\n")
	return;


def doBGM(line,output_file):
#
# This is the Beginning of Message segment
#
# An example of this segment is as follows:
# BGM+220::9:DELIVERY+59661+9'
# 
# The Layout of this segment is as follows:
# Document Message Name
#	Document Name Code
#	Code List ID
#	Code List Responsible Agency Code
#	Document Name
# Document Identifier
# Message Function Code
#
# Get rid of the last 2 characters on the line 
#
	line = line[:-2]
#	
# Splitting the fields
#
	split_list = line.split("+")
	segment_identifier				= split_list[0]
#	
	document_message_name			= split_list[1]
	split_sub						= document_message_name.split(":")
	document_name_code				= split_sub[0]
	code_list_id					= split_sub[1]
	responsible_agency_cd			= split_sub[2]
	document_name 					= split_sub[3]
#	
	document_identifier				= split_list[2]
#
	message_function_code			= split_list[3]
#	
# Write the XML Structure to the file
#	
	output_file.write("	<" + segment_identifier + ">\r\n")
	output_file.write("		<DocumentMessageName> \r\n")
	output_file.write("			<DocumentNameCode>" + document_name_code + "</DocumentNameCode> \r\n")
	output_file.write("			<CodeListID>" + code_list_id + "</CodeListID> \r\n")
	output_file.write("			<ResponsibleAgencyCode>" + responsible_agency_cd + "</ResponsibleAgencyCode> \r\n")
	output_file.write("			<DocumentName>" + document_name  + "</DocumentName> \r\n")
	output_file.write("		</DocumentMessageName> \r\n")
	output_file.write("		<DocumentIdentifier>" + document_identifier	 + "</DocumentIdentifier> \r\n")
	output_file.write("		<MessageFunctionCode>" + message_function_code + "</MessageFunctionCode> \r\n")
	output_file.write("	</" + segment_identifier + ">\r\n")
	return;

def doDTM(line,output_file):
#
# This is the Date Time segment
#
# An example of this segment is as follows:
# DTM+137:201503231130:203'
# DTM+2:201503251130:203'# 
#
# The file layout of this segment is as follows:
# Date Time Period
#	Period Function Code Qualifier
#	Period Value
#	Period Format Code
#
# Get rid of the last 2 characters on the line 
#
	line = line[:-2]
#	
# Splitting the fields
#	
	split_list = line.split("+")
	segment_identifier				= split_list[0]
	
	date_time_period				= split_list[1]
	split_sub						= date_time_period.split(":")
	period_function_code_qualifier	= split_sub[0]
	period_value					= split_sub[1]
	period_format_code				= split_sub[2]
#	
# Write the XML Structure to the file
#	
	output_file.write("	<" + segment_identifier + ">\r\n")
	output_file.write("		<DateTimePeriod> \r\n")
	output_file.write("			<PeriodFunctionCodeQualifier>" + period_function_code_qualifier + "</PeriodFunctionCodeQualifier> \r\n")
	output_file.write("			<PeriodValue>" + period_value + "</PeriodValue> \r\n")
	output_file.write("			<PeriodFormatCode>" + period_format_code + "</PeriodFormatCode> \r\n")
	output_file.write("		</DateTimePeriod> \r\n")
	output_file.write("	</" + segment_identifier + ">\r\n")
	return;

def doFTX(line,output_file):
#
# This is the Free Text segment
#
# An example of this segment is as follows:
# FTX+PUR+++ORDER NOTES'
# FTX+PKG+++Europalette'
# 
# The file layout of this segment is as follows:
# Text Subject Code Qualifier
# Free Text Function Code
# Text Reference
# Text Literal
#
# Get rid of the last 2 characters on the line 
#
	line = line[:-2]
#	
# Splitting the fields
#	
	split_list = line.split("+")
	segment_identifier				= split_list[0]
	text_subject_code_qualifier		= split_list[1]
	free_text_function_code			= split_list[2]
	text_reference					= split_list[3]
	text_literal					= split_list[4]	
#	
# Write the XML Structure to the file
#	
	output_file.write("	<" + segment_identifier + ">\r\n")
	output_file.write("		<TextSubjectCodeQualifier>" + text_subject_code_qualifier + "</TextSubjectCodeQualifier> \r\n")
	output_file.write("		<FreeTextFunctionCode>" + free_text_function_code + "</FreeTextFunctionCode> \r\n")	
	output_file.write("		<TextReference>" + text_reference + "</TextReference> \r\n")
	output_file.write("		<TextLiteral>" + text_literal + "</TextLiteral> \r\n")
	output_file.write("	</" + segment_identifier + ">\r\n")
	return;


def doRFF(line,output_file):
#
# This is the Reference segment
#
# An example of this segment is as follows:
# RFF+SZ:NNN-00042/59665'
# RFF+YC1:12345'
# 
# The file layout of this segment is as follows:
# Reference
# 	Reference Code Qualifier
#	Reference Identifier
#
# Get rid of the last 2 characters on the line 
#
	line = line[:-2]
#	
# Splitting the fields
#	
	split_list = line.split("+")
	segment_identifier				= split_list[0]
#	
	reference 						= split_list[1]
	split_sub						= reference.split(":")
	reference_code_qualifier		= split_sub[0]
	reference_identifier			= split_sub[1]
#	
# Write the XML Structure to the file
#	
	output_file.write("	<" + segment_identifier + ">\r\n")
	output_file.write("		<Reference> \r\n")
	output_file.write("			<ReferenceCodeQualifier>" + reference_code_qualifier + "</ReferenceCodeQualifier> \r\n")
	output_file.write("			<ReferenceIdentifier>" + reference_identifier + "</ReferenceIdentifier> \r\n")	
	output_file.write("		</Reference> \r\n")
	output_file.write("	</" + segment_identifier + ">\r\n")
	return;
#
def doNAD(line,output_file):
#
# This is the Name and Address segment
#
# An example of this segment is as follows:
# NAD+BY+4399902114486::9++ALDI REGION+ALDI STREET 1+ALDI CITY+NRW+46045+DE'
# NAD+SU+5412345678908::9++SUPPLIER+SUPPLIER STREET 1+SUPPLIER CITY+NRW+46047+DE'
# NAD+HP+5412345678908::9++MESSAGE RECIPIENT+RECIPIENT STREET 1+RECIPIENT CITY++46049+DE'
# NAD+DP+4399902114486::9++ALDI WAREHOUSE+ALDI STREET 1+ALDI CITY++46045+DE'
# 
# The file layout of this segment is as follows:
# Party Function Code Qualifier
# Party Identification Details
# 	Party Identifier
#	Code List ID Code
#	Responsible Agency Code
# Name and Address
# Party Name
# Street
# City Name
# Country Sub Entity Name Code
# Postal ID Code
# Country Name code
#
# Get rid of the last 2 characters on the line 
#
	line = line[:-2]
#	
# Splitting the fields
#	
	split_list = line.split("+")
	segment_identifier				= split_list[0]
	party_function_code_qualifier 	= split_list[1]
#
	party_identification_details	= split_list[2]
	split_sub						= party_identification_details.split(":")
	party_identifier				= split_sub[0]
	code_list_id_code				= split_sub[1]
	responsible_agency_code			= split_sub[2]

	name_and_address				= split_list[3]
	party_name						= split_list[4]
	street 						 	= split_list[5]
	city_name						= split_list[6]
	country_sub_entity_name_code 	= split_list[7]
	postal_id_code					= split_list[8]
	country_name_code 				= split_list[9]
#	
# Write the XML Structure to the file
#	
	output_file.write("	<" + segment_identifier + ">\r\n")
	output_file.write("		<PartyFunctionCodeQualifier>" + party_function_code_qualifier + "</PartyFunctionCodeQualifier> \r\n")
	output_file.write("		<PartyIdentificationDetails> \r\n")
	output_file.write("			<PartyIdentifier>" + party_identifier + "</PartyIdentifier> \r\n")	
	output_file.write("			<CodeListIDCode>" + code_list_id_code + "</CodeListIDCode> \r\n")	
	output_file.write("			<ResponsibleAgencyCode>" + responsible_agency_code + "</ResponsibleAgencyCode> \r\n")	
	output_file.write("		</PartyIdentificationDetails> \r\n")
	output_file.write("		<NameAndAddress>" + name_and_address + "</NameAndAddress> \r\n")
	output_file.write("		<PartyName>" + party_name + "</PartyName> \r\n")
	output_file.write("		<Street>" + street + "</Street> \r\n")
	output_file.write("		<CityName>" + city_name  + "</CityName> \r\n")
	output_file.write("		<CountrySubEntityNameCode>" + country_sub_entity_name_code + "</CountrySubEntityNameCode> \r\n")
	output_file.write("		<PostalIDCode>" + postal_id_code + "</PostalIDCode> \r\n")
	output_file.write("		<CountryNameCode>" + country_name_code + "</CountryNameCode> \r\n")
	output_file.write("	</" + segment_identifier + ">\r\n")
	return;
#
def doCTA(line,output_file):
#
# An example of this segment is as follows:
# CTA+PD+:MR. SMITH'
# 
# The Layout of this segment is as follows:
# Contact Function Code
# Contact Details
#		Contact Name Code
# 		Contact Name
#
# Get rid of the last 2 characters on the line 
#
	line = line[:-2]
#	
# Splitting the fields
#	
	
	split_list = line.split("+")
	segment_identifier				= split_list[0]
	contact_function_code 			= split_list[1]

	contact_details					= split_list[2]
	split_sub						= contact_details.split(":")
	contact_name_code				= split_sub[0]
	contact_name 					= split_sub[1]
	
# Write the XML Structure to the file
#	
	output_file.write("	<" + segment_identifier + ">\r\n")
	output_file.write("		<ContactFunctionCode>" + contact_function_code + "</ContactFunctionCode> \r\n")
	output_file.write("		<ContactDetails> \r\n")
	output_file.write("			<ContactNameCode>" + contact_name_code + "</ContactNameCode> \r\n")	
	output_file.write("			<ContactName>" + contact_name + "</ContactName> \r\n")	
	output_file.write("		</ContactDetails> \r\n")
	output_file.write("	</" + segment_identifier + ">\r\n")
	return;
# 
def doCOM(line,output_file):
#
# An example of this segment is as follows:
# COM+00492081111111:TE'
# COM+00492082222222:FX'
# COM+CONTACT@ALDI-SUED.COM:FX'
# 
# The Layout of this segment is as follows:
# Communication Contact
# 		Communication Address Identifier
#		Communication Address Code Qualifier
#	
	print ("***************************************************************************************************************************************")
	line = line[:-2]
	print ("Line 					: " + line)
	print ("***************************************************************************************************************************************")
#	
# Splitting the fields
#	
	split_list = line.split("+")
	segment_identifier				= split_list[0]
	communication_contact 			= split_list[1]
	split_sub						= communication_contact.split(":")
	address_identifier				= split_sub[0]
	address_code_qualifier 			= split_sub[1]
#	
# Printing the fields
#
	print ("Segment Identifier 			: " + segment_identifier)
	print ("Address Identifier  			: " + address_identifier)
	print ("Address Code Qualifier			: " + address_code_qualifier)
	print(" ")
	return;
# 
def doLIN(line,output_file):
#
# An example of this segment is as follows:
# LIN+1'
# 
# The Layout of this segment is as follows:
# Line Item Identifier
#	
	print ("***************************************************************************************************************************************")
	line = line[:-2]
	print ("Line 					: " + line)
	print ("***************************************************************************************************************************************")
#	
# Splitting the fields
#	
	split_list = line.split("+")
	segment_identifier				= split_list[0]
	line_item_identifier 			= split_list[1]
#	
# Printing the fields
#
	print ("Segment Identifier 			: " + segment_identifier)
	print ("Line Item Identifier  			: " + line_item_identifier)
	print(" ")
	return;
#
def doPIA(line,output_file):
#
# An example of this segment is as follows:
# PIA+5+12345:IN::92'
# PIA+1+DE-54321:XY8::92'
# 
# The Layout of this segment is as follows:
# Product Identifier
# Item Number ID
# 		Item ID
#		Item Type ID Code
#		Code List ID Code
#		Responsible Agency Code
#	
	print ("***************************************************************************************************************************************")
	line = line[:-2]
	print ("Line 					: " + line)
	print ("***************************************************************************************************************************************")
#	
# Splitting the fields
#	
	split_list = line.split("+")
	segment_identifier				= split_list[0]
	product_identifier				= split_list[1]
	item_number_ID 			 		= split_list[2]
	split_sub						= item_number_ID.split(":")
	item_ID 						= split_sub[0]
	item_type_ID_code				= split_sub[1]
	code_list_ID_code 				= split_sub[2]
	responsible_agency_code			= split_sub[3]
#	
# Printing the fields
#
	print ("Segment Identifier 			: " + segment_identifier)
	print ("Product Identifier 			: " + product_identifier)
	print ("Item ID 		  		: " + item_ID)
	print ("Item Type ID Code  	  		: " + item_type_ID_code)
	print ("Code List ID Code 	  		: " + code_list_ID_code)
	print ("Responsible Agency Code		  	: " + responsible_agency_code)
	print(" ")
	return;
# 
def doIMD(line,output_file):
#
# An example of this segment is as follows:
# IMD+F++:::MUESLI'
# 
# The Layout of this segment is as follows:
# Description Format Code
# Item Characteristic
# Item Description 
#		Item Description Code
#		Code List ID Code
#		Responsible Agency Code
#		Item Description
#	
	print ("***************************************************************************************************************************************")
	line = line[:-2]
	print ("Line 					: " + line)
	print ("***************************************************************************************************************************************")
#	
# Splitting the fields
#	
	split_list = line.split("+")
	segment_identifier				= split_list[0]
	description_format_code			= split_list[1]
	item_characteristic				= split_list[2]
	item_description_tl				= split_list[3]
	split_sub						= item_description_tl.split(":")
	item_description_code			= split_sub[0]
	code_list_ID_code 				= split_sub[1]
	responsible_agency_code			= split_sub[2] 
	item_description 				= split_sub[3]
#	
# Printing the fields
#
	print ("Segment Identifier 			: " + segment_identifier)
	print ("Description Format Code			: " + description_format_code)
	print ("Item Characteristic		 	: " + item_characteristic)
	print ("Item Description Code  	  		: " + item_description_code)
	print ("Code List ID Code 	  		: " + code_list_ID_code)
	print ("Responsible Agency Code		  	: " + responsible_agency_code)
	print ("Item Description 		  	: " + item_description )
	print(" ")
	return;
# 
def doQTY(line,output_file):
#
# An example of this segment is as follows:
# QTY+21:48:200'
# QTY+45E:5760:CS'
# # 
# The Layout of this segment is as follows:
# Quantity Details
#		Quantity Type Code Qualifier
#		Quantity
#		Measurement Unit Code
#
	print ("***************************************************************************************************************************************")
	line = line[:-2]
	print ("Line 					: " + line)
	print ("***************************************************************************************************************************************")
#	
# Splitting the fields
#	
	split_list = line.split("+")
	segment_identifier				= split_list[0]
	quantity_details				= split_list[1]
	split_sub						= quantity_details.split(":")
	quantity_type_code_qualifier	= split_sub[0]
	quantity 		 				= split_sub[1]
	measurement_unit_code			= split_sub[2] 
#	
# Printing the fields
#
	print ("Segment Identifier 			: " + segment_identifier)
	print ("Quantity Type Code Qualifier		: " + quantity_type_code_qualifier)
	print ("Quantity	 			: " + quantity)
	print ("Measurement Unit Code  	  		: " + measurement_unit_code)
	print(" ")
	return;
#
def doUNS(line,output_file):
#
# An example of this segment is as follows:
# UNS+S'
# 
# The Layout of this segment is as follows:
# Section ID
#	
	print ("***************************************************************************************************************************************")
	line = line[:-2]
	print ("Line 					: " + line)
	print ("***************************************************************************************************************************************")
#	
# Splitting the fields
#	
	split_list = line.split("+")
	segment_identifier				= split_list[0]
	section_ID			 			= split_list[1]
#	
# Printing the fields
#
	print ("Segment Identifier 			: " + segment_identifier)
	print ("Section ID   				: " + section_ID)
	print(" ")
	return;
# 
def doCNT(line,output_file):
#
# An example of this segment is as follows:
# CNT+16:48'
#
# The Layout of this segment is as follows:
# Control
#		Control Total Type Code Qualifier
#		Control Total Value
#
	print ("***************************************************************************************************************************************")
	line = line[:-2]
	print ("Line 					: " + line)
	print ("***************************************************************************************************************************************")
#	
# Splitting the fields
#	
	split_list = line.split("+")
	segment_identifier					= split_list[0]
	control 							= split_list[1]
	split_sub							= control.split(":")
	control_total_type_code_qualifier	= split_sub[0]
	control_total_value 		 		= split_sub[1]
#	
# Printing the fields
#
	print ("Segment Identifier 			: " + segment_identifier)
	print ("Control Total Type Code Qualifier	: " + control_total_type_code_qualifier)
	print ("Control Total Value 			: " + control_total_value )
	print(" ")
	return;
# 
def doUNT(line,output_file):
#
# An example of this segment is as follows:
# UNT+26+54322'
# 
# The Layout of this segment is as follows:
# Number of Segments
# Message Reference Number
#
	print ("***************************************************************************************************************************************")
	line = line[:-2]
	print ("Line 					: " + line)
	print ("***************************************************************************************************************************************")
#	
# Splitting the fields
#	
	split_list = line.split("+")
	segment_identifier					= split_list[0]
	number_of_segments 					= split_list[1]
	message_reference_number 			= split_list[2]
#	
# Printing the fields
#
	print ("Segment Identifier 			: " + segment_identifier)
	print ("Number of Segments			: " + number_of_segments)
	print ("Message Reference Number		: " + message_reference_number)
	print(" ")
	return;
#
def doUNZ(line,output_file):
#
# An example of this segment is as follows:
# UNZ+1+12345552'
# 
# The Layout of this segment is as follows:
# Interchange Control Count
# Interchange Control Reference
#
	print ("***************************************************************************************************************************************")
	line = line[:-2]
	print ("Line 					: " + line)
	print ("***************************************************************************************************************************************")
#	
# Splitting the fields
#	
	split_list = line.split("+")
	segment_identifier					= split_list[0]
	interchange_control_count 			= split_list[1]
	interchange_control_reference		= split_list[2]
#	
# Printing the fields
#
	print ("Segment Identifier 			: " + segment_identifier)
	print ("Interchange Control Count		: " + interchange_control_count)
	print ("Interchange Control Reference		: " + interchange_control_reference)
	print(" ")
	return;
#

def segment_names(segment,line,output_file):
	switcher = {
		"UNA" : doUNA,
		"UNB" : doUNB,
		"UNH" : doUNH,
		"BGM" : doBGM,
		"DTM" : doDTM,
		"FTX" : doFTX,
		"RFF" : doRFF,
		"NAD" : doNAD,
		"CTA" : doCTA,
		"COM" : doCOM,
		"LIN" : doLIN,
		"PIA" : doPIA,
		"IMD" : doIMD,
		"QTY" : doQTY,
		"UNS" : doUNS,
		"CNT" : doCNT,
		"UNT" : doUNT,
		"UNZ" : doUNZ,
	}
	# Get the function name from switcher dictionary
	# Parse each line based on EDIFACT Segment rules
	switcher.get(segment, "Invalid segment")(line,output_file)
#	
def input_file_name ():
	# set up the input file path. Not elegant as it will only work on my Mac but we can work on this later. CI an all!
	filepath = "/Users/Johann/Documents/Coding/Python/Input Files/ALDI_EDIFACT_Order_File.txt"
	print("Read from File : " + filepath)
	return filepath;

def open_output_file ():
	# Set up the Output file path. Not elegant as it will only work on my Mac but we can work on this later. CI an all!
	filepath = "/Users/Johann/Documents/Coding/Python/Output Files/ALDI_EDIFACT_Order_File.xml"
	
	# Create the XMl Output File
	output_file = open(filepath,"w+")
	print("Output To File : " + filepath)
	return output_file;

def XML_pre_amble (output_file):
	output_file.write('<?xml version="1.0" encoding="UTF-8"?>\r\n')
	output_file.write("<ORDER>\r\n")
	return;

def XML_close_tag (output_file):
	output_file.write("</ORDER>")
	return;

def read_file():
	# Open the Output File and make it ready for use.
	output_file = open_output_file()
	
	# Write the first line of XML to the file
	XML_pre_amble(output_file)

	# Open the EDIFACT Input FIle
	with open(input_file_name()) as file: 	

		# now read the file Line by line
	   	for count, line in enumerate(file):
	   		FirstThree = line[0:3]
	   		
	   		# Set Up the Switcher Directory
	   		segment_names(FirstThree,line,output_file)

	# Write the last line of XML to the file
	XML_close_tag(output_file)
	# Close the File
	output_file.close()
	return;

def main():
	# read the file so we can parse it
	read_file()
	return;


# ****************************************************************************************************************************************************************************
# This is the main section of the script
#
main()
#
# ****************************************************************************************************************************************************************************