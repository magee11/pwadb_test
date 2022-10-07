import datetime
from flask import Blueprint,request
import flask
project_view = Blueprint('project',__name__,url_prefix='/api/v1/projects')
from .models import Project,Weekly_reports
from registrations.build_app import db
import boto3
import os 
from flask import request 
import traceback


# # api for weekly_reports
# @project.route('/weekly',methods=['GET', 'POST'])
# def create_reports():
#     # print("data")
#     if flask.request.method == 'POST':
#         weekly_report_obj = Weekly_reports()
#         db.session.add(assign_data_to_weekly_rep_obj(request.json,weekly_report_obj))
#         db.session.commit()
#     return "Weekly_reports Summitted Successfully"
    

# # api for edit the weekly reports
# @project.route('/weekly_reports/<id>', methods=['PUT'])
# def edit_reports(id):
#     update_record = Weekly_reports.query.get(id)

#     assign_data_to_weekly_rep_obj(request.json, update_record)
#     print(update_record.start_data)



# # func for get value to field
# def assign_data_to_weekly_rep_obj(payload,weekly_reports_obj):
#     if 'start_data' in payload and payload['start_data']:
#         weekly_reports_obj.start_data = payload['start_data']
#     if 'end_date' in payload and payload['end_date']:
#         weekly_reports_obj.end_date = payload['end_date']
#     if 'no_stories' in payload and payload['no_stories']:
#         weekly_reports_obj.no_stories = payload['no_stories']
#     if 'features_completed' in payload and payload['features_completed']:
#         weekly_reports_obj.features_completed = payload['features_completed']
#     if 'no_bugs' in payload and payload['no_bugs']:
#         weekly_reports_obj.no_bugs = payload['no_bugs']
#     if 'bug_complete' in payload and payload['bug_complete']:
#         weekly_reports_obj.bug_compltet = payload['bug_complete']
#     if 'code_review' in payload and payload['code_review']:
#         weekly_reports_obj.code_review = payload['start_data']
#     if 'unit_testing' in payload and payload['unit_testing']:
#         weekly_reports_obj.unit_testing = payload['unit_testing']
#     if 'weekly_communication' in payload and payload['weekly_communication']:
#         weekly_reports_obj.weekly_communication = payload['weekly_communication']
#     if 'migration' in payload and payload['migration']:
#         weekly_reports_obj.migration = payload['migration']
#     if 'risk' in payload and payload['risk']:
#         weekly_reports_obj.risk = payload['risk']
#     if 'risk_migration' in payload and payload['risk_migration']:
#         weekly_reports_obj.risk_migration = payload['risk_migration']
#     if 'support_required' in payload and payload['support_required']:
#         weekly_reports_obj.support_required = payload['support_required']
#     if 'project_id' in payload and payload['project_id']:
#         weekly_reports_obj.project_id = payload['project_id']
#     return weekly_reports_obj


@project_view.route('/create', methods=['GET','POST'])
def create_reports():
        if request.method == 'POST':
         data = request.json
         start_date = data['startDate']
         end_date = data['endDate']
         no_stories = data['noOfStories']
         features_completed = data['featuresCompleted']
         no_bugs = data['noOfBugs']
         bugs_complete = data['bugsCompleted']
         is_code_review = data['isCodeReviewDone']
         is_unit_testing = data['isUnitTestingDone']
         weekly_communication = data['isWeeklyCommunicationDone']
         risk = data['risks']
         risk_migration = data['riskMitigation']
        support_required = data['supportRequired']
        new_record = Weekly_reports(start_date =start_date, end_date =end_date,no_stories = no_stories,features_completed = features_completed, 
        no_bugs = no_bugs, bugs_complete = bugs_complete, is_code_review = is_code_review,is_unit_testing = is_unit_testing,weekly_communication = weekly_communication,
        risk =risk,risk_migration = risk_migration,support_required = support_required)
           
        db.session.add(new_record)
        db.session.commit()
        return {"content":"Added successfully","error":0,"message":"success"}




# update_record for Weekly_reports API (PUT)

@project_view.route('/edit/<_id>', methods=['PUT'])
def edit_report(_id):
        data_edit = request.get_json()
        get_report =  Weekly_reports.query.get(_id)
        if data_edit.get('startDate'):
            get_report.start_date = data_edit['startDate']
        if data_edit.get('endDate'):
            get_report.end_date = data_edit['endDate']
        if data_edit.get('no_stories'):
            get_report.no_stories = data_edit['no_stories']
        if data_edit.get('features_completed'):
            get_report.features_completed = data_edit['features_completed']
        if data_edit.get('no_bugs'):
            get_report.no_bugs = data_edit['no_bugs']
        if data_edit.get('is_code_review'):
            get_report.is_code_review = data_edit['is_code_review']
        if data_edit.get('is_unit_testing'):
            get_report.is_unit_testing = data_edit['is_unit_testing']
        if data_edit.get('weekly_communication'):
            get_report.weekly_communication = data_edit['weekly_communication']
        if data_edit.get('risk'):
            get_report.risk = data_edit['risk']
        if data_edit.get('risk_migration'):
            get_report.risk_migration = data_edit['risk_migration']
        if data_edit.get('support_required'):   
            get_report.support_required = data_edit['support_required']
        db.session.add(get_report)
        db.session.commit()
        return {"content":"Added successfully","error":0,"message":"success"}











        

@project_view.route('/upload_image',methods=['POST'])
def upload_image():
    try:
        print("fkjrkf")
        image_file = request.files['file']
        raw = image_file.read()
        filename = image_file.filename
        g=upload_to_s3(filename,obj=raw)
        # 'https://'+bucketname+'.s3.'+region_name+'.amazonaws.com/'+filename)
        return f'https://{os.getenv("bucket")}.s3.{os.getenv("AWS_DEFAULT_REGION")}.amazonaws.com/{filename}'
        # return {"content":"Added successfully","error":0,"message":"success"}

    except Exception as e:
        print(traceback.print_exc())
        return {"content":"Added successfully","error":str(e),"message":"success"}
def upload_to_s3(name,obj=None):
    client = boto3.client(
    's3',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_DEFAULT_REGION"))  

    # client.upload_file(filepath, bucket, filename, ExtraArgs = {'ACL':'public-read'})
    p = client.put_object(Body=obj, Bucket=os.getenv("bucket"), Key=name , ACL = 'public-read' )

    print(p,type(p))
    return "s"