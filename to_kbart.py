import csv
from collections import defaultdict
import sys
import os

def to_kbart(provider_file):
	csv.field_size_limit(sys.maxsize)
	filename = os.path.join(os.getcwd(), provider_file)
	return_filename = os.path.splitext(filename)[0]+'_kbart.txt'
	results =[]
	kbart = defaultdict(lambda : '')
	kbart_header = [
	"publication_title",  
	"print_identifier", 
	"online_identifier", 
	"date_first_issue_online", 
	"num_first_vol_online", 
	"num_first_issue_online", 
	"date_last_issue_online", 
	"num_last_vol_online", 
	"num_last_issue_online", 
	"title_url", 
	"first_author", 
	"title_id", 
	"embargo_info", 
	"coverage_depth", 
	"coverage_notes", 
	"publisher_name", 
	"location", 
	"title_notes", 
	"staff_notes", 
	"oclc_collection_name", 
	"oclc_collection_id",  
	"oclc_entry_id", 
	"oclc_linkscheme", 
	"oclc_number", 
	"ACTION"
	]

	with open(filename, 'rU') as f_in: 
		dictreader = csv.DictReader(f_in)
		for row in dictreader:
			for value in kbart_header:
				try:
					kbart[value] = row[value]
				except KeyError:
					pass
			result = [kbart[value] for value in kbart_header]
			results.append(result)

	with open(return_filename, 'wb') as f_out:
		writer = csv.writer(f_out, dialect = 'excel-tab')
		writer.writerow(kbart_header)
		for item in results:
			writer.writerow(item)

if __name__ == "__main__":
to_kbart(sys.argv[1])