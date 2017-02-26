
#!/usr/bin/env python3
print('Content-type: text/html\r\n\r')

    import cgitb
    import cgi
    import PIL	

    cgitb.enable() 

    inputs = cgi.FieldStorage() 
    resize = inputs.getvalue("effect")


    print "Content-type: text/html" 

    print "<title> MyPythonWebpage </title>"

    from PIL import Image

	# SM = Social media

Social media = {

	Youtube = {
	
	'SMYoutube_Banner' : im.resize((2048, 1152))
	
	'SMYoutbe_channel_icon' : im.resize((800, 800))
	
	'SMYoutube_video_thumbnail' : im.resize((1280, 720))

	}

	Twitter = {
	
	'SMTwitter_header' : im.resize((1500, 500))
	
	'SMTwitter_profile' : im.resize((400, 400))

	'SMTwitter_tweeted_image' : im.resize((1024, 512))

	}

	Facebook = { 

	'SMFacebook_cover_photo_desktop' : im.resize((828, 315))

	'SMFacebook_cover_photo_mobile' : im.resize((828, 465))
	
	'SMFacebook_profile_photo' : im.resize((180, 180))

	'SMFacebook_thumbnail' : im.resize((111, 74))
	
	'SMFacebook_link_preview' : im.resize((600, 314))
	
	'SMFacebook_photo_post' : im.resize((504, 504))

		## missing --- Facebook Group Cover photo ---
	
	'SMFacebook_cover_photo_desktop' : im.resize((128, 128))

	'SMFacebook_event_cover_photo' : im.resize((1200, 675))

	}


	Google+ = {

	'SMGoogleplus_cover_photo' : im.resize((1080, 608))

	'SMGoogleplus_profile_photo' : im.resize((250, 250))
	}

	LinkedIn = {

	'SMLinkedin_background' : im.resize((1400, 425))

	'SMLinkedin_profile_photo' : im.resize((500, 500))

	'SMLinkedin_status_update' : im.resize((700, 400))

	'SMLinkedin_company_cover_photo' : im.resize((1536, 768))

	'SMLinkedin_logo' : im.resize((400, 400))


	Pinterest = {

	'SMPinterest_profile_photo': im.resize((180, 180))

	'SMPinterest_board_cover' : im.resize((214, 100))
	}

	Instagram = {

	'SMInstagram_profile_photo' : im.resize((110, 110))

	'SMInstagram_photo' : im.resize((1080))
	}

}




Advertisment = {

	Billboard art sizes = {
		
	'Ad4sheet' : im.resize((1016, 1524))
	
	'Ad6sheet' : im.resize((1200, 1800))
	
	'Ad12sheet' : im.resize((3048, 1524))
		
	'Ad16sheet' : im.resize((2032, 3048))
		
	'Ad32sheet' : im.resize((4064, 3048))
		
	'Ad48sheet' : im.resize((6096, 3048))
		
	'Ad64sheet' : im.resize((8128, 3048))

	'Ad96sheet' : im.resize((12192, 3048))
	}

Icon = {               
	
	'Icon_android' : im.resize((57, 57))

	}

Physical = {
		
	'Physical_passport' : im.resize((51, 51))

	'Physical_photo_id' : im.resize((128, 128))

	'Physical_family_portrait' : im.resize((128, 128))

	'Physical_drivers_license' : im.resize((128, 128))
}
