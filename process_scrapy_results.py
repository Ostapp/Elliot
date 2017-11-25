	def open_json_results():
		with open('items_emails_10.json','r') as f:
			results = json.load(f)
		return results

	def open_json_requests():
		with open('emails.json','r') as f:
			results = json.load(f)
		return results

	def extract_domain(url):
		extracted = tldextract.extract(url)
		domain = "{}.{}".format(extracted.domain, extracted.suffix)
		return domain

	def process_spider_results(spider_results):
		results = {}
		# spider_results = open_json_results()
		for item in spider_results:
			domain = extract_domain(item['url'])
			email = set()
			if ".png" in item['email']:
				pass
			elif ".jpg" in item['email']:
				pass
			else:
				email.add(item['email'])
				results[domain] = results.get(domain, set()).union(email)
		return results

	def save_emails(emails):
		with open ('final_emails.pickle', 'w') as f:
			pickle.dump(emails, f)

	def save_matches(matches):
		with open ('new_matches.pickle', 'w') as f:
			pickle.dump(matches, f)

	def load_pickled_file(filename):
		with open (filename, 'r') as f:
			result = pickle.load(f)
			return result

	def load_json_file(filename):
		with open (filename, 'r') as f:
			result = json.load(f)
			return result

def make_xlsx_file_emails(results_dict):

	workbook = xlsxwriter.Workbook('Damian_emails.xlsx')
	worksheet = workbook.add_worksheet()

	row = 0

	for key, value in results_dict.items():
		final_string = ""
		for url in value:
			if len(value) > 1:
				if len(final_string) > 0:
					final_string = final_string + ", " + url
				else:
					final_string = url
				print final_string
			else:
				final_string = url
				print 'else'
		worksheet.write_string(row, 0, key)
		worksheet.write_string(row, 1, final_string)
		row +=1

	workbook.close()
