def check_user(role, l_status, venue):
    if l_status == False and if session.get("l-status") == True:
            return redirect(url_for(venue))
    if l_status == True:
        if not session.get("l-status"):
            return redirect(url_for(venue))
        if venue != "any":
            if session.get("role") != venue:
                return redirect(request.referrer or url_for(venue))
