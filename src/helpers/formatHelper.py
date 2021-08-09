from src.helpers.githubHelper import parse_ticket_id, parse_github_user

def format_comment(user, pr,comment):
    """ Format passed github comment in this 
    ["Track", "Sprint", "US","Developer","Reviwed By","ReviewedDate","Category","PR Link", "Comment", "Severity","Remark","Mitigation Plan","Target Date"]
    format. """
    formattedComment = []
    #Track 
    formattedComment.append("")
    #Sprint 
    formattedComment.append("")
    #US
    formattedComment.append(parse_ticket_id(pr.title))
    #Developer
    formattedComment.append(' '.join(user.name.split(',')))
    #Reviwed By
    formattedComment.append(parse_github_user(comment.user.url))
    #ReviewedDate
    formattedComment.append(comment.created_at.strftime("%Y-%m-%d"))
    #Category
    formattedComment.append("")
    #PR Link
    formattedComment.append(pr.html_url)
    #Comment
    formattedComment.append(comment.body.encode("unicode_escape").decode("utf-8"))
    #Severity
    formattedComment.append("")
    #Remark
    formattedComment.append("")
    #Mitigation Plan
    formattedComment.append("")
    #Target Date
    formattedComment.append("")

    return formattedComment

def format_list_to_csv(list):
    rows = [];
    column_seprator = ','
    row_seprator = '\n'

    for idx, item in enumerate(list):
        if idx == 0:
            continue
        rows.append(column_seprator.join(item))
    
    return row_seprator.join(rows)
