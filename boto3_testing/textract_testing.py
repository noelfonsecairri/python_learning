import boto3, pprint

textract_client = boto3.client("textract")



s3_object = {'Bucket': 'noelbeerbucket', 'Name': '2019 | John,K | Earthworms offset straw-induced increase of greenhouse gas emission in upland rice production.pdf'}

get_job_id = textract_client.start_document_text_detection(DocumentLocation={'S3Object': s3_object})

#pprint.pprint(get_job_id)

response = textract_client.get_document_text_detection(JobId=get_job_id['JobId'])

start_doc_analysis = textract_client.start_document_analysis(DocumentLocation={'S3Object': s3_object}, FeatureTypes=['TABLES','FORMS',])


#pprint.pprint(start_doc_analysis)

get_doc_analysis = textract_client.get_document_analysis(JobId=start_doc_analysis['JobId'])

pprint.pprint(response)
#print(get_doc_analysis['JobStatus'])
pprint.pprint(get_doc_analysis)