import csv
import json
import requests
import time


class IterableAPI():
	"""
	This is a python wrapper for the Iterable API

	We are using the Requests HTTP python library, which I 
	have found flexible in regards to the arguments you
	can pass into each request.  Their documentation is 
	also excellent.  This makes it must easier in the event I were to 
	expand this wrapper to encompass all the possible Iterable API requests.

	"""	

	def __init__(self, api_key):
		"""
		This preforms all initialization and stores the unique API key of the
		Iterable instance. It also stores the base URI, which is consistent
		for all instances.

		"""
		
		self.base_uri = "https://api.iterable.com"		
		self.api_key = api_key

	def api_call(self, call, method, params=None, headers=None, data=None,
				 json=None):
		"""
		This is our generic api call function.  We will route all our calls
		through this function.  The benefit of this is that it:
			1. Allows for easier debugging if a request fails
			2. Even though the Iterable API only needs the API key for a 
			security standpoint, if it were ever to require access token for 
			each request we could easily manage the granting and expiration
			management of such a token.  

		"""

		# params(optional) Dictionary or bytes to be sent in the query string for the Request.
		if params is None:
			params = {}
		# headers- dictionary of HTTP Headers to be sent with Request
		if headers is None:
			headers = {}
		# data- dict or list of tuples to be sent in body of Request
		if data is None:
			data = {}
		# json- data to be sent in body of Request
		if json is None:
			json ={}		
		
		headers["Content-type"] = "application/json"
		headers["Api-Key"] = self.api_key

		# make the request following the 'requests.request' method
		r = requests.request(method=method, url=self.base_uri+call, params=params,
							 headers=headers, data=data, json=json)
		
		# for debugging-- want 401 error without API key
		
		if (r.status_code == 200):
			return r.json()

		else:
			print(r.status_code)

	"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

	Iterable Campaign Requests

	"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

	def list_campaign_info(self):

		call="/api/campaigns"

		return self.api_call(call=call, method="GET")

	def create_campaign(self, name=None, list_ids=None, template_id=None,
						suppression_list_ids=None, send_at=None,
						send_mode=None, start_time_zone=None,
						default_time_zone=None, data_fields=None):

		call = "/api/capaigns/create"

		payload ={}

		if name is not None:
			payload["name"]= str(name)

		if list_ids is not None:
			payload["listIds"]= list_ids

		if template_id is not None:
			payload["template_id"]= template_id

		if suppression_list_ids is not None:
			payload["supressionListIds"]= suppression_list_ids

		if send_at is not None:
			payload["sendAt"]= str(send_at)

		if send_mode is not None:
			payload["sendMode"]= str(send_mode)

		if start_time_zone is not None:
			payload["startTimeZone"]= str(start_time_zone)

		if default_time_zone is not None:
			payload["defaultTimeZone"]= str(default_time_zone)

		if data_fields is not None:
			payload["dataField"]= data_fields


		return self.api_call(call=call, method="POST", json=payload)

	def get_campaign_metrics(self, campaign_id=None, start_date_time=None,
							 end_date_time=None, use_new_format=None):

		call= "/api/campaigns/metrics"

		payload ={}

		if campaign_id is not None:
			payload["campaignId"]= campaign_id

		if start_date_time is not None:
			payload["startDateTime"]= str(start_date_time)

		if end_date_time is not None:
			payload["endDateTime"]= str(end_date_time)

		if use_new_format is not None:
			payload["useNewFormat"]= use_new_format


		return self.api_call(call=call, method="GET", params=payload)

	def get_child_campaigns(self, campaign_id=None):

		if campaign_id is not None:
			call = "/api/campaigns/recurring/"+str(campaign_id)+"/childCampaigns"


		return self.api_call(call=call, method="GET")


	"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

	Iterable Channel Requests


	"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

	def list_channels(self):

		call="/api/channels"

		return self.api_call(call=call, method="GET")

	"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

	Iterable Commerce Reqeusts

	"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

	def track_purchase(self, user=None, items=None, campaign_id=None, 
					   template_id=None, total=None, created_at=None,
					   data_fields=None):

		call="/api/commerce/trackPurchase"

		payload ={}

		if user is not None:
			payload["user"]= user

		if items is not None:
			payload["items"]= items

		if campaign_id is not None:
			payload["campaignId"]= campaign_id

		if template_id is not None:
			payload["templateId"]= template_id

		if total is not None:
			payload["total"]= total

		if created_at is not None:
			payload["createdAt"]= created_at

		if data_fields is not None:
			payload["data_fields"]= data_fields

		return self.api_call(call=call, method="POST", json=payload)

	def update_cart(self, user=None, items=None):

		call="/api/commerce/updateCart"

		payload ={}

		if user is not None:
			payload["user"]= user

		if items is not None:
			payload["items"]= items

		return self.api_call(call=call, method="POST", json=payload)

	"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

	Iterable Email Requests

	"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

	def send_email(self, campaign_id=None, recipient_email=None,
				   data_fields=None, send_at=None,
				   allow_repeat_marketing_sends=None, metadata=None,
				   message_medium=None, icon_class=None, name=None):

		call="/api/email/target"

		payload ={}

		if campaign_id is not None:
			payload["campaignId"]= campaign_id

		if recipient_email is not None:
			payload["recipientEmail"]= str(recipient_email)

		if data_fields is not None:
			payload["dataFields"]= data_fields

		if send_at is not None:
			payload["sendAt"]= send_at

		if allow_repeat_marketing_sends is not None:
			payload["allowRepeatMarketingSends"]= allow_repeat_marketing_sends

		if metadata is not None:
			payload["metadata"]= metadata

		if message_medium is not None:
			payload["messageMedium"]= message_medium

		if icon_class is not None:
			payload["iconClass"]= icon_class

		if name is not None:
			payload["name"]= name


		return self.api_call(call=call, method="POST", json=payload)

	def view_email_in_browser(self, email=None, message_id=None):

		call = "/api/email/viewInBrowser"

		payload ={}

		if email is not None:
			payload["email"]= email

		if message_id is not None:
			payload["messageId"]= message_id

		return self.api_call(call=call, method="GET", params=payload)

	"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

		Iterable Event Requests

	"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

	def get_events(self, email=None, limit=None):

		call="/api/events/"+str(email)

		payload={}

		if (limit is not None
		 		and limit < 200):
			payload["limit"]= limit

		return self.api_call(call=call, method="GET", parms=payload)

	def consume_in_app_notification(self, email=None, user_id=None,
									message_id=None, button_index=None):

		call = "/api/events/inAppConsume"

		payload ={}

		if email is not None:
			payload["email"]=email

		if user_id is not None:
			payload["userId"]=user_id

		if message_id is not None:
			payload["messageId"]= message_id

		if button_index is not None:
			payload["buttonIndex"]= button_index

		return self.api_call(call=call, method="POST", json=payload)

	def track_event(self, email=None, event_name=None, created_at=None,
					data_fields=None, user_id=None, campaign_id=None,
					template_id=None):

		call="/api/events/track"

		payload={}

		if email is not None:
			payload["email"]=email

		if event_name is not None:
			payload["eventName"]=event_name

		if created_at is not None:
			payload["createdAt"]=created_at

		if data_fields is not None:
			payload["dataFields"]= data_fields

		if user_id is not None:
			payload["userId"]=user_id

		if campaign_id is not None:
			payload["campaignId"]= campaign_id

		if template_id is not None:
			payload["templateId"]= template_id

		return self.api_call(call=call, method="POST", json=payload)

	def track_in_app_click(self, email=None, user_id=None,
						   message_id=None, button_index=None):

		call="/api/events/trackInAppClick"

		payload={}

		if email is not None:
			payload["email"]= email

		if user_id is not None:
			payload["userId"]=user_id

		if message_id is not None:
			payload["messageId"]=message_id

		if button_index is not None:
			payload["buttonIndex"]=button_index

		return self.api_call(call=call, method="POST", json=payload)

	def track_in_app_open(self, email=None, user_id=None, message_id=None,
						  button_index=None):

		call="/api/events/trackInAppOpen"

		payload={}

		if email is not None:
			payload["email"]= email

		if user_id is not None:
			payload["userId"]=user_id

		if message_id is not None:
			payload["messageId"]=message_id

		if button_index is not None:
			payload["buttonIndex"]=button_index

		return self.api_call(call=call, method="POST", json=payload)

	def track_push_open(self, email=None, user_id=None, campaign_id=None,
						template_id=None, message_id=None, created_at=None,
						data_fields=None):

		call="/api/events/trackPushOpen"

		payload={}

		if email is not None:
			payload["email"]=email

		if user_id is not None:
			payload["userId"]=user_id

		if campaign_id is not None:
			payload["CampaignId"]= campaign_id

		if template_id is not None:
			payload["templateId"]=template_id

		if message_id is not None:
			payload["messageId"]=message_id

		if created_at is not None:
			payload["createdAt"]= created_at

		if data_fields is not None:
			payload["dataFields"]=data_fields

		return self.api_call(call=call, method="POST", json=payload)

	def track_web_push_click(self, email=None, user_id=None,
							 message_id=None, campaign_id=None,
							 template_id=None):

		call ="/api/events/trackWebPushClick" 

		payload={}

		if email is not None:
			payload["email"]=email

		if user_id is not None:
			payload["userId"]=user_id

		if message_id is not None:
			payload["messageId"]=message_id

		if campaign_id is not None:
			payload["campaignId"]=campaign_id

		if template_id is not None:
			payload["templateId"]=template_id

		return self.api_call(call=call, method="POST", json=payload)

	"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
		
	Iterable Experiment Requests

	"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

	def get_experiment_metrics(self, experiment_id=None, campaign_id=None,
							   start_date_time=None, end_date_time=None):

		call="/api/experiments/metrics"

		payload={}

		if experiment_id is not None:
			payload["experimentId"]=experiment_id

		if campaign_id is not None:
			payload["campaignId"]=campaign_id

		if start_date_time is not None:
			payload["startDateTime"]=start_date_time

		if end_date_time is not None:
			payload["endDateTime"]=end_date_time

		return self.api_call(call=call, method="GET", params=payload)


	"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
	
	Export Data Requests

	"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

	def export_data_csv(self, data_type_name=None, date_range=None,
						delimiter=None):

		call="/api/export/data.csv"

		payload={}

		if data_type_name is not None:
			payload["dataTypeName"]= data_type_name

		if date_range is not None:
			payload["range"]= date_range

		if delimiter is not None:
			payload["delimiter"]= delimiter

		return self.api_call(call=call, method="GET", params=payload)

	def export_data_json(self, data_type_name=None, date_range=None,
						 delimiter=None):

		call="/api/export/data.json"

		payload={}

		if data_type_name is not None:
			payload["dataTypeName"]= data_type_name

		if date_range is not None:
			payload["range"]= date_range

		if delimiter is not None:
			payload["delimiter"]= delimiter

		return self.api_call(call=call, method="GET", params=payload)


	"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
	
	Iterable inApp Requests

	"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

	def get_in_app_messages(self, email=None, user_id=None, count=None,
							platform=None, sdk_version=None):

		call = "/api/inApp/getMessages"

		payload={}

		if email is not None:
			payload["email"]=str(email)

		if user_id is not None:
			payload["userId"]=str(user_id)

		if count is not None:
			payload["count"]=count

		if platform is not None:
			payload["platform"]=str(platform)

		if sdk_version is not None:
			payload["SDKVersion"]= sdk_version

		return self.api_call(call=call, method="GET", params=payload)

	def send_in_app_notification(self, campaign_id=None, recipient_email=None,
								 data_fields=None, send_at=None,
								 message_medium=None,
								 allow_repeat_marketing_sends=None):

		call="/api/inApp/target"

		payload={}

		if campaign_id is not None:
			payload["campaignId"]=campaign_id

		if recipient_email is not None:
			payload["recipientEmail"]=recipient_email

		if data_fields is not None:
			payload["dataFields"]=data_fields

		if send_at is not None:
			payload["sendAt"]=send_at

		if allow_repeat_marketing_sends is not None:
			payload["allowRepeatMarketingSends"]= allow_repeat_marketing_sends

		if message_medium is not None:
			payload["messageMedium"]=message_medium

		return self.api_call(call=call, method="POST", json=payload)

	"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
		
		Iterable List requests


	"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

	def get_lists(self):

		call = "/api/lists"

		return self.api_call(call=call, method="GET")

	def create_list(self, list_name=None):

		call = "/api/lists"

		payload ={}

		if list_name is not None:
			payload["name"]= str(list_name)

		return self.api_call(call="call", method="POST", json=payload)

	def delete_static_list(self, list_id=None):

		call = "/api/lists/"+str(list_id)

		return self.api_call(call=call, method="DELETE")

	def number_of_users_in_list(self, list_id=None):

		call = "/api/lists/"+str(list_id)+"/size"

		return self.api_call(call=call, method="GET")

	def get_users_in_list(self, list_id=None):

		call = "/api/lists/getUsers"

		payload ={}

		if list_id is not None:
			payload["listId"]= list_id

		return self.api_call(call=call, method="GET", params=payload)

	def add_subscribers_to_list(self, list_id=None, subscribers=None):

		call = "/api/lists/subscribe"

		payload = {}

		if list_id is not None:
			payload["listId"]= list_id

		if subscribers is not None:
			payload["subscribers"]= subscribers

		return self.api_call(call=call, method="POST", json=payload)

	def remove_subscribers_to_list(self, list_id=None, subscribers=None,
								   campaign_id=None, channel_unsubscribe=False):

		call = "/api/lists/unsubscribe"

		payload = {}

		if list_id is not None:
			payload["listId"]= list_id

		if subscribers is not None:
			payload["subscribers"]= subscribers

		if campaign_id is not None:
			payload["campaignId"]= campaign_id

		if channel_unsubscribe is not None:
			payload["channelUnsubscribe"]= channel_unsubscribe

		return self.api_call(call=call, method="POST", json=payload)

	"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
	
	Iterable MessageType Requests


	"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

	def list_message_types(self):

		call="/api/messageTypes"

		return self.api_call(call=call, method="GET")

	"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

	Iterable Metadata Requests


	"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
	
	def list_available_tables(self):

		call="/api/metadata"

		return self.api_call(call=call, method="GET")

	def delete_all_metadata_from_table(self, table=None):

		if table is not None:
			call="/api/metadata"+str(table)

		return self.api_call(call=call, method="DELETE")

	def list_keys_in_table(self, table=None, next_marker=None):

		if table is not None:
			call= "/api/metadata/"+str(table)

		payload ={}

		if next_marker is not None:
			payload["nextMarket"]=next_marker

		return self.api_call(call=call, method="GET", params=payload)

	def delete_single_metadata_key_value(self, table=None, key=None):
		
		if table is not None and key is not None:
			call="/api/metadata/"+ str(table) + "/" + str(key)

		return self.api_call(call=call, method="DELETE")

	def get_single_metadata_key_value(self, table=None, key=None):

		if table is not None and key is not None:
			call="/api/metadata/"+ str(table) + "/" + str(key)

		return self.api_call(call=call, method="GET")

	def create_or_replace_metadata(self, table=None, key=None, value=None):

		if table is not None and key is not None:
			call="/api/metadata/"+ str(table) + "/" + str(key)

		payload={}

		if value is not None:
			payload["value"]= value

		return self.api_call(call=call, method="PUT", json=payload)

	"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

	Iterable Push Requests

	"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

	def send_push_notification(self, campaign_id=None, 
							   recipient_email=None, data_fields=None,
							   send_at=None, 
							   allow_repeat_marketing_sends=None,
							   message_medium=None):

		call="/api/push/target"

		payload={}

		if campaign_id is not None:
			payload["campaignId"]= campaign_id

		if recipient_email is not None:
			payload["recipientEmail"]= recipient_email

		if data_fields is not None:
			payload["dataFields"]= data_fields

		if send_at is not None:
			payload["sendAt"]= send_at

		if allow_repeat_marketing_sends is not None:
			payload["allowRepeatMarketingSends"]= allow_repeat_marketing_sends

		if message_medium is not None:
			payload["messageMedium"]= message_medium

		return self.api_call(call=call, method="POST", json=payload)

	"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

	Iterable SMS Requests

	"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

	def send_sms_message(self, campaign_id=None, 
					     recipient_email=None, data_fields=None,
					     send_at=None, 
					     allow_repeat_marketing_sends=None,
					     message_medium=None):

		call="/api/sms/target"

		payload={}

		if campaign_id is not None:
			payload["campaignId"]= campaign_id

		if recipient_email is not None:
			payload["recipientEmail"]= recipient_email

		if data_fields is not None:
			payload["dataFields"]= data_fields

		if send_at is not None:
			payload["sendAt"]= send_at

		if allow_repeat_marketing_sends is not None:
			payload["allowRepeatMarketingSends"]= allow_repeat_marketing_sends

		if message_medium is not None:
			payload["messageMedium"]= message_medium

		return self.api_call(call=call, method="POST", json=payload) 

	"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

	Iterable Template Requests

	"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

	def get_templates_for_project(self, template_type=None, 
								  message_medium=None,
								  start_date_time=None,
								  end_date_time=None):

		call="/api/templates"

		payload={}

		if template_type is ("Base" or "Blast" or "Triggered" or "Workflow"):
			payload["templateType"]=template_type	

		else:
			raise ValueError('You did not specify the correct template type')

		if message_medium is ("Email" or "Push" or "InApp" or "SMS"):
			payload["messageMedium"]=message_medium

		else:
			raise ValueError('You did not specify the correct message medium')

		if start_date_time is not None:
			payload["startDateTime"]=start_date_time

		if end_date_time is not None:
			payload["endDateTime"]= end_date_time

		return self.api_call(call=call, method="GET", params=payload)

	def get_email_template(self, template_id=None, locale=None):

		call="/api/templates/email/get"

		payload={}

		if template_id is not None:
			payload["templateId"]=template_id

		if locale is not None:
			payload["locale"]= locale

		return self.api_call(call=call, method="GET", params=payload)

	def update_email_template(self, template_id=None, metadata=None,
							  name=None, from_name=None, from_email=None,
							  reply_to_email=None, subject=None,
							  preheader_text=None, cc_emails=None,
							  bcc_emails=None, html=None,
							  plain_text=None,
							  google_analytics_campaign_name=None,
							  link_parameters=None, data_feed_id=None,
							  cache_data_feed=None,
							  merge_data_feed_context=None,
							  client_template_id=None, locale=None,
							  message_type_id=None, creator_user_id=None):


		call="/api/templates/email/update"

		payload={}

		if template_id is not None:
			payload["templateId"]= template_id

		if metadata is not None:
			payload["metadata"]= metadata

		if name is not None:
			payload["name"]= name

		if from_name is not None:
			payload["fromName"]= from_name

		if from_email is not None:
			payload["fromEmail"]= from_email

		if reply_to_email is not None:
			payload["replyToEmail"]= reply_to_email

		if subject is not None:
			payload["subject"]= subject

		if preheader_text is not None:
			payload["preheaderText"]= preheader_text

		if cc_emails is not None:
			payload["ccEmails"]= cc_emails

		if bcc_emails is not None:
			payload["bccEmails"]= bcc_emails

		if html is not None:
			payload["html"]= html

		if plain_text is not None:
			payload["planText"]= plain_text

		if google_analytics_campaign_name is not None:
			payload["googleAnalyticsCampaignName"]= google_analytics_campaign_name

		if link_parameters is not None:
			payload["linkParameters"]= link_parameters

		if data_feed_id is not None:
			payload["dataFeedId"]= data_feed_id

		if cache_data_feed is not None:
			payload["cacheDataFeed"]= cache_data_feed

		if merge_data_feed_context is not None:
			payload["mergeDataFeedContext"]= merge_data_feed_context

		if client_template_id is not None:
			payload["clientTemplateId"]= client_template_id

		if locale is not None:
			payload["locale"]= locale

		if message_type_id is not None:
			payload["messageTypeId"]= message_type_id

		if creator_user_id is not None:
			payload["creatorUserId"]= creator_user_id

		return self.api_call(call=call, method="POST", json=payload)

	def upsert_email_template(self, client_template_id=None,
							  name=None, from_name=None, from_email=None,
							  reply_to_email=None, subject=None,
							  preheader_text=None, cc_emails=None,
							  bcc_emails=None, html=None,
							  plain_text=None,
							  google_analytics_campaign_name=None,
							  link_parameters=None, data_feed_id=None,
							  cache_data_feed=None,
							  merge_data_feed_context=None,
							  locale=None,
							  message_type_id=None, creator_user_id=None):

		call="/api/templates/email/upsert"

		payload={}

		if client_template_id is not None:
			payload["clientTemplateId"]= client_template_id

		if name is not None:
			payload["name"]= name

		if from_name is not None:
			payload["fromName"]= from_name

		if from_email is not None:
			payload["fromEmail"]= from_email

		if reply_to_email is not None:
			payload["replyToEmail"]= reply_to_email

		if subject is not None:
			payload["subject"]= subject

		if preheader_text is not None:
			payload["preheaderText"]= preheader_text

		if cc_emails is not None:
			payload["ccEmails"]= cc_emails

		if bcc_emails is not None:
			payload["bccEmails"]= bcc_emails

		if html is not None:
			payload["html"]= html

		if plain_text is not None:
			payload["planText"]= plain_text

		if google_analytics_campaign_name is not None:
			payload["googleAnalyticsCampaignName"]= google_analytics_campaign_name

		if link_parameters is not None:
			payload["linkParameters"]= link_parameters

		if data_feed_id is not None:
			payload["dataFeedId"]= data_feed_id

		if cache_data_feed is not None:
			payload["cacheDataFeed"]= cache_data_feed

		if merge_data_feed_context is not None:
			payload["mergeDataFeedContext"]= merge_data_feed_context

		if locale is not None:
			payload["locale"]= locale

		if message_type_id is not None:
			payload["messageTypeId"]= message_type_id

		if creator_user_id is not None:
			payload["creatorUserId"]= creator_user_id

		return self.api_call(call=call, method="POST", json=payload)

	def get_email_template(self, client_template_id=None):

		call="/api/templates/getClientTemplateId"

		payload={}

		if client_template_id is not None:
			payload["clientTemplateId"]= client_template_id

		return self.api_call(call=call, method="GET", params=payload)

	def get_push_template(self, template_id=None, locale=None):

		call="/api/templates/push/get"

		payload={}

		if template_id is not None:
			payload["templateId"]= template_id

		if locale is not None:
			payload["locale"]= locale

		return self.api_call(call=call, method="GET", params=payload)

	def update_push_template(self, template_id=None, created_at=None,
							 updated_at=None, name=None, message=None,
							 payload_content=None, badge=None, locale=None,
							 message_type_id=None, sound=None,
							 deeplink=None, client_template_id=None,
							 campaign_id=None):

		call="/api/templates/push/update"

		payload = {}

		if template_id is not None:
			payload["templateId"]= template_id

		if created_at is not None:
			payload["createdAt"]= created_at

		if updated_at is not None:
			payload["updatedAt"]= updated_at

		if name is not None:
			payload["name"]= name

		if message is not None:
			payload["message"]= message

		if payload_content is not None:
			payload["payload"]= payload_content

		if badge is not None:
			payload["badge"]= badge

		if locale is not None:
			payload["locale"]= locale

		if message_type_id is not None:
			payload["messageTypeId"]= message_type_id

		if sound is not None:
			payload["sound"]= sound

		if deeplink is not None:
			payload["deeplink"]= deeplink

		if client_template_id is not None:
			payload["clientTemplateId"]= client_template_id

		if campaign_id is not None:
			payload["campaignId"]= campaign_id

		return self.api_call(call=call, method="POST", json=payload)

	def upsert_push_template(self, client_template_id=None, name=None,
							 message=None, payload_content=None, 
							 badge=None, locale=None,
							 message_type_id=None, sound=None,
							 deeplink=None, campaign_id=None):

		call="/api/templates/push/upsert"

		payload = {}

		if client_template_id is not None:
			payload["clientTemplateId"]= client_template_id

		if name is not None:
			payload["name"]= name

		if message is not None:
			payload["message"]= message

		if payload_content is not None:
			payload["payload"]= payload_content

		if badge is not None:
			payload["badge"]= badge

		if locale is not None:
			payload["locale"]= locale

		if message_type_id is not None:
			payload["messageTypeId"]= message_type_id

		if sound is not None:
			payload["sound"]= sound

		if deeplink is not None:
			payload["deeplink"]= deeplink

		if campaign_id is not None:
			payload["campaignId"]= campaign_id

		return self.api_call(call=call, method="POST", json=payload)

	def get_sms_template(self, template_id=None, locale=None):

		call="/api/templates/sms/get"

		payload={}

		if template_id is not None:
			payload["templateId"]= template_id

		if locale is not None:
			payload["locale"]= locale

		return self.api_call(call=call, method="GET", params=payload)

	def update_sms_template(self, template_id=None, created_at=None,
							updated_at=None, name=None, message=None,
							locale=None, message_type_id=None,
							image_url=None, client_template_id=None,
							campaign_id=None):

		call="/api/templates/sms/update"

		payload= {}

		if template_id is not None:
			payload["templateId"]= template_id

		if created_at is not None:
			payload["createdAt"]= created_at

		if updated_at is not None:
			payload["updatedAt"]= updated_at

		if name is not None:
			payload["name"]= name

		if message is not None:
			payload["message"]= message

		if locale is not None:
			payload["locale"]= locale

		if message_type_id is not None:
			payload["messageTypeId"]= message_type_id

		if image_url is not None:
			payload["imageUrl"]= image_url

		if client_template_id is not None:
			payload["clientTemplateId"]= client_template_id

		if campaign_id is not None:
			payload["campaignId"]= campaign_id

		return self.api_call(call=call, method="POST", json=payload)


	def upsert_sms_template(self, client_template_id=None,
							name=None, message=None, locale=None,
							message_type_id=None, image_url=None,
							campaign_id=None):

		call="/api/templates/sms/upsert"

		payload= {}

		if client_template_id is not None:
			payload["clientTemplateId"]= client_template_id

		if name is not None:
			payload["name"]= name

		if message is not None:
			payload["message"]= message

		if locale is not None:
			payload["locale"]= locale

		if message_type_id is not None:
			payload["messageTypeId"]= message_type_id

		if image_url is not None:
			payload["imageUrl"]= image_url

		if campaign_id is not None:
			payload["campaignId"]= campaign_id

		return self.api_call(call=call, method="POST", json=payload)

			

	"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

	Iterable User Requests


	"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

	def delete_user(self, email=None):
	
		"""
		This call will delete a user from the Iterable database.  
		This call requires a path parameter to be passed in, 'email'
		in this case, which is why we're just adding this to the 'call'
		argument that goes into the 'api_call' request. 		
		"""
		if email is not None:
			call = "/api/users/"+ str(email)

		return self.api_call(call=call, method="DELETE")

	def get_user_by_email(self, email=None):
		"""This function gets a user's data field and info"""

		if email is not None:
			call = "/api/users/"+ str(email)

		return self.api_call(call=call, method="GET")

	def bulk_update_user(self, users):

		"""
		The Iterable 'Bulk User Update' api Bulk update user data or adds 
		it if does not exist. Data is merged - missing fields are not deleted

		The body of the request takes 1 keys:
			1. users -- in the form of an array -- which is the list of users
				that we're updating in sets of 50 users at a time, which is the 
				most that can be batched in a single request.  
		"""

		call = "/api/users/bulkUpdate"		
		
		payload = {}

		if users is not None:
			payload["users"] = users		

		return self.api_call(call=call, method="POST", json=payload)

	def bulk_update_subscriptions(self, update_subscriptions_requests=None):

		call ="/api/users/bulkUpdateSubscriptions"

		payload = {}

		if update_subscriptions_requests is not None:
			payload["updateSubscriptionsRequests"] = update_subscriptions_requests

		return self.api_call(call=call, method="POST", json=payload)

	def get_users_by_userid(self, user_id=None):

		call = "/api/users/byUserId"

		payload ={}

		if user_id is not None:
			payload["userId"] = user_id

		return self.api_call(call=call, method="GET", params=payload)

	def delete_users_by_userid_userid(self, user_id=None):

		if user_id is not None:
			call = "/api/users/byUserId/"+str(user_id)			

		return self.api_call(call=call, method="DELETE")

	def get_users_by_userid_userid(self, user_id):

		if user_id is not None:
			call = "/api/users/byUserId/" + str(user_id)

		return self.api_call(call=call, method="GET")

	def disable_device(self, token=None, email=None, user_id=None):
		"""
		This request manually disable pushes to a device until it comes
		online again.

		"""

		call = "/api/users/disableDevice"

		payload ={}

		if token is not None:
			payload["token"] = str(token)

		if email is not None:	
			payload["email"] = str(email)

		if user_id is not None:
			payload["userId"] = str(user_id)

		return self.api_call(call= call, method="POST", json=payload)

	def get_user_by_email(self, email=None):

		call = "/api/users/getByEmail"

		payload = {}

		if email is not None:
			payload["email"]= email

		return self.api_call(call=call, method="GET", params=payload)

	def get_user_fields(self):

		call = "api/users/getFields"

		return self.api_call(call=call, method="GET")

	def get_sent_messages(self, email=None, user_id=None, limit=None,
						  campaign_id=None, start_date_time=None,
						  end_date_time=None, exclude_blast_campaigns=None,
						  message_medium=None):
		"""

		campaign_id takes an Array[double] as a query parameter...what
		does this mean x=[[1,2,3],[4,5,6]]?

		"""

		call = "/api/users/getSentMessages"

		channels = ["Email", "Push", "InApp", "SMS"]

		payload ={}

		if email is not None:
			payload["email"] = str(email)

		if user_id is not None:
			payload["userId"]= str(user_id)

		if limit is not None:
			payload["limit"]= int(limit)

		if campaign_id is not None:
			payload["campaignId"]= campaign_id

		if start_date_time is not None:
			payload["startDateTime"]= start_date_time

		if end_date_time is not None:
			payload["endDateTime"]= end_date_time

		if exclude_blast_campaigns is not None:
			payload["excludeBlastCampaigns"]= exclude_blast_campaigns

		if message_medium is not None and message_medium in channels:
			payload["messageMedium"]= str(message_medium)

		return self.api_call(call=call, method="GET", params=payload)

	def register_browser_token(self, email=None, browser_token=None,
							   user_id=None):

		call = "/api/users/registerBrowserToken"

		payload= {}

		if email is not None:
			payload["email"]= email

		if browser_token is not None:
			payload["browserToken"] = browser_token

		if user_id is not None:
			payload["userId"]= user_id

		return self.api_call(call=call, method="POST", json=payload)

	def register_device_token(self, email=None, device_token=None,
							  user_id=None):

		call = "/api/users/registerDeviceToken"

		payload = {}

		if email is not None:
			payload["email"]= email

		if device_token is not None:
			payload["device"] = device_token

		if user_id is not None:
			payload["userId"] = user_id

		return self.api_call(call=call, method="POST", json=payload)

	def update_user(self, email=None, data_fields=None, user_id=None,
					merge_nested_objects=None):

		"""
		The Iterable 'User Update' api updates a user profile with new data 
		fields. Missing fields are not deleted and new data is merged.

		The body of the request takes 4 keys:
			1. email-- in the form of a string -- used as the unique identifier by
				the Iterable database.
			2. data fields-- in the form of an object-- these are the additional attributes
			 of the user that we want to add or update
			3. userId- in the form of a string-- another field we can use as a lookup
				of the user. 
			4. mergeNestedObjects-- in the form of an object-- used to merge top level
				objects instead of overwriting. 
		"""

		call = "/api/users/update"
		
		payload = {}

		if email is not None:
			payload["email"] = str(email)

		if data_fields is not None:
			payload["dataFields"] = data_fields

		if user_id is not None:
			payload["userId"] = str(user_id)

		if merge_nested_objects is not None:
			payload["mergeNestedObjects"] = merge_nested_objects
		
		return self.api_call(call=call, method="POST", json=payload)

	def update_email(self, current_email=None, new_email=None):

		call = "/api/users/updateEmail"

		payload = {}

		if current_email is not None:
			payload["currentEmail"] = current_email

		if new_email is not None:
			payload["newEmail"] = new_email

		return self.api_call(call=call, method="POST", json=payload)

	def update_subscriptions(self, email=None, email_list_ids=None,
							 unsubscribed_channel_ids=None,
							 unsubscribed_message_type_ids=None,
							 campaign_id=None, template_id=None):

		call="/api/users/updateSubscriptions"

		payload ={}

		if email is not None:
			payload["email"]= email

		if email_list_ids is not None:
			payload["emailListIds"]

		if unsubscribed_channel_ids is not None:
			payload["unsubscribedChannelIds"]= unsubscribed_channel_ids

		if unsubscribed_message_type_ids is not None:
			payload["unsubscribedMessageTypeIds"]= unsubscribed_message_type_ids

		if campaign_id is not None:
			payload["campaignId"] = campaign_id

		if template_id is not None:
			payload["templateId"]= template_id

		return self.api_call(call=call, method="POST", json=payload)

	"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

	Iterable Web Push Requests

	"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

	def send_web_push_notification(self, campaign_id=None, 
							       recipient_email=None, data_fields=None,
							       send_at=None, 
							       allow_repeat_marketing_sends=None,
							       message_medium=None):

		call="/api/webPush/target"

		payload={}

		if campaign_id is not None:
			payload["campaignId"]= campaign_id

		if recipient_email is not None:
			payload["recipientEmail"]= recipient_email

		if data_fields is not None:
			payload["dataFields"]= data_fields

		if send_at is not None:
			payload["sendAt"]= send_at

		if allow_repeat_marketing_sends is not None:
			payload["allowRepeatMarketingSends"]= allow_repeat_marketing_sends

		if message_medium is not None:
			payload["messageMedium"]= message_medium

		return self.api_call(call=call, method="POST", json=payload)

	"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

	Iterable Workflow Requests

	"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

	def trigger_workflow(self, email=None, workflow_id=None,
						 data_fields=None, list_id=None):

		call="/api/workflows/triggerWorkflow"

		payload={}

		if email is not None:
			payload["email"]= email

		if workflow_id is not None:
			payload["workflowId"]= workflow_id

		if data_fields is not None:
			payload["dataFields"]=data_fields

		if list_id is not None:
			payload["listId"]= list_id

		return self.api_call(call=call, method="POST", json=payload)



	