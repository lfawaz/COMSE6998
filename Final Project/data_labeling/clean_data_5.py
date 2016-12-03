def clean_data(text_str):
	if type(text_str) is list:
		text_str = " ".join(text_list)
	if text_str == 'A e s t h e t i c':
		text_str = 'Aesthetic'
	text_str = text_str.replace('\xe2\x84\xa2', '')
	#text.str = text_str.replace('\xe2', '')
	text_str = text_str.replace('\n', '')
	text_str = text_str.replace('&', '')
	text_str = text_str.replace('[', '')
	text_str = text_str.replace(']', '')
	text_str = text_str.replace('#', '')
	text_str = text_str.replace('@', '')
	text_str = text_str.replace('%', '')
	text_str = text_str.replace('$', '')
	text_str = text_str.replace('{', '')
	text_str = text_str.replace('}', '')
	text_str = text_str.replace('\'', '')
	text_str = text_str.replace('*', '')
	text_str = text_str.replace('/', '')
	text_str = text_str.replace('(https:www.reddit.comrsamsungcomments51iuahslugd7cg30h)!', '')
	text_str = text_str.replace('\xf0\x9f\x98\x82\xf0\x9f\x98\x82', '')
	text_str = text_str.replace('!', '.')
	text_str = text_str.replace('"', '')
	text_str = text_str.replace('http:imgur.comIggVgYu And then... http:imgur.coma8QsUf', '')
	text_str = text_str.replace(':http:imgur.comIpCTAwDhttp:imgur.comOS0JdfK', '')
	text_str = text_str.replace(' https:www.google.commapsplace44C2B05722.422N+93C2B01903.922W44.9562169,-93.3182952,19zdata=.3m1.4b1.4m5.3m4.1s0x0:0x0.8m2.3d44.956216.4d-93.317748Is ', '')
	text_str = text_str.replace('http:imgur.comIpCTAwD http:imgur.comOS0JdfK ', '')
	text_str = text_str.replace('http:www.bbc.co.uknewstechnology-31709198 ', '')
	text_str = text_str.replace('-', ' ')
	text_str = text_str.replace(':', ' ')
	text_str = text_str.replace('(Xda(http:forum.xda-developers.comgalaxy-s7helppaypal-problems-t3331894) and the Paypal community forum(https:www.paypal-community.comt5About-ProductsSamsung-Galaxy-S7-Edge-Fingerprint-Issuetd-p1045067))', '')
	text_str = text_str.replace(')', '')
	text_str = text_str.replace('(', '')
	text_str = text_str.replace('http www.theverge.com20169112759912samsung', ' ')
	text_str = text_str.replace(';', '')
	text_str = text_str.replace('amp;039;s Yonhap News Agency.gt; Yonhap claims that ', ' ')
	text_str = text_str.replace('Summaryhttp np.reddit.comrautotldrcomments50qwedthe_verge_samsung_will_reportedly_issue_worldwide | FAQhttp np.reddit.comrautotldrcomments31b9fmfaq_autotldr_bot Version 1.6, ~97092 tldrs so far. | Theoryhttp np.reddit.comrautotldrcomments31bfhttheory_autotldr_concept | Feedbackhttp np.reddit.commessagecompose?to=23autotldr PMs and comment replies are read by the bot admin, constructive feedback is welcome. | Top keywords  Samsung^1 Note^2 recall^3 company^4 reports^5', '')
	text_str = text_str.replace('=', '')
	text_str = text_str.replace('http i.imgur.comj75vIc8.png', '')
	text_str = text_str.replace('~', '')
	text_str = text_str.replace(' www.youtube.comwatch?vEV1DreF97Ys', '')
	text_str = text_str.replace('www.banggood.comAUDEW Q5 Universal Qi Wireless Charger Charging Pad Transmitter p 985122.html', '')
	text_str = text_str.replace('Banggood.com', '')
	text_str = text_str.replace('http www.phonearena.comnewsSamsung', '')
	text_str = text_str.replace('imgur.comjmJ4Vtf', '')
	text_str = text_str.replace('http www.theverge.com201652311743594microsoft', '')
	text_str = text_str.replace('Ded rglitch_art \xef\xbc\xa1\xef\xbd\x85\xef\xbd\x93\xef\xbd\x94\xef\xbd\x88\xef\xbd\x85\xef\xbd\x94\xef\xbd\x89\xef\xbd\x83', '')
	text_str = text_str.replace('\\ New Pictureshttp imgur.com9h8hZA7http imgur.com5lGjTHthttp imgur.comG1VpGjIhttp imgur.comrC5hBPOhttp imgur.comEgNoNPnhttp imgur.comanZlCDN ', '')
	text_str = text_str.replace('FLAT.. COME TO MEEEEEEEEEE ', '')
	text_str = text_str.replace('www.youtube.comwatch?vNdyH22ojXyUhttp www.trustedreviews.comnewsgalaxy ', '')
	text_str = text_str.replace('it\xe2\x80\x99s', '')
	text_str = text_str.replace(',', '')
	text_str = text_str.replace('deleted   ^^^^^^^^^^^^^^^^0.9306  gt What is this?https pastebin.com64GuVi2F05097 ', '')
	text_str = text_str.replace('www.cnet.comhow', '')
	text_str = text_str.replace(' 6 0 marshmallow.reboot phone.Should work', ' ')
	text_str = text_str.replace('?', '.')
	text_str = text_str.replace('Extended Summaryhttp np.reddit.comrautotldrcomments57jc5kfaa_bans_all_samsung_galaxy_note_7s_from_us | FAQhttp np.reddit.comrautotldrcomments31b9fmfaq_autotldr_bot Version 1.65 6380 tldrs so far. | Theoryhttp np.reddit.comrautotldrcomments31bfhttheory_autotldr_concept | Feedbackhttp np.reddit.commessagecompose.to23autotldr PMs and comments are monitored constructive feedback is welcome. | Top keywords  phone^1 Samsung^2 ban^3 airline^4 passenger^5', ' ')
	text_str = text_str.replace('Samsung Offerhttps promos.samsungpromotions.comgearvren usEnterVerizonPurchase aSamsung Galaxy S7 or Galaxy S7 edgeon a device payment planon VZW.com.VisitSamsungPromotions.comVerizonOfferto', ' ')
	text_str = text_str.replace('\xc2\xa0location code', ' ')
	text_str = text_str.replace(' Samsung.com\xe2\x80\xa0.\xe2\x80\xa0Coupon code only valid for purchases made on Samsung.com 32316 \xe2\x80\x93 7116', ' ')
	text_str = text_str.replace('\xe2\x80\x99', ' ')
	text_str = text_str.replace('APKhttps drive.google.comfiled0B6Izh2mlcYLiaG9FMTJ0YWo2cm8view.uspdrivesdk', ' ')
	text_str = text_str.replace('\xf0\x9f\x98\x92 ', '.')
	text_str = text_str.replace('http economictimes.indiatimes.commagazinespanachesamsung galaxy s8 to have ai digital assistant servicearticleshow55270507.cms reduced by 62', '')
	text_str = text_str.replace(' 7amp039s', '')
	text_str = text_str.replace('Extended Summaryhttp np.reddit.comrautotldrcomments5bfz0xsamsung_galaxy_s8_to_have_ai_digital_assistant | FAQhttp np.reddit.comrautotldrcomments31b9fmfaq_autotldr_bot Version 1.65 16057 tldrs so far. | Theoryhttp np.reddit.comrautotldrcomments31bfhttheory_autotldr_concept | Feedbackhttp np.reddit.commessagecompose.to23autotldr PMs and comments are monitored constructive feedback is welcome. | Top keywords  Galaxy^1 Samsung^2 service^3 assistant^4 smartphone^5 Imagehttp imgs.xkcd.comcomicsstandards.pngMobilehttps m.xkcd.com927Title  StandardsTitle text  Fortunately the charging one has been solved now that weve all standardized on mini\\ USB\\. Or is it micro\\ USB. Shit\\.Comic Explanationhttps www.explainxkcd.comwikiindex.php927ExplanationStats  This comic has been referenced 3790 times representing 2.8249 of referenced xkcds.   ^xkcd.comhttps www.xkcd.com ^| ^xkcd\xc2\xa0subhttps www.reddit.comrxkcd ^| ^ProblemsBugs.https www.reddit.comrxkcd_transcriber ^| ^Statisticshttp xkcdref.infostatistics ^| ^Stop\xc2\xa0Replyinghttps reddit.commessagecompose.toxkcd_transcriberampsubjectignore20meampmessageignore20me ^| ^Deletehttps reddit.commessagecompose.toxkcd_transcriberampsubjectdeleteampmessagedelete20t1_d9o3qei ', '')
	text_str = text_str.replace(' http i.imgur.comk5Gc6vj.gifv Thank you  Galaxy Note 7 announcement liveblog_id83755 Anyone having live streaming interruptions and disconnect on the non 360 video. Its getting annoying.Edit  This is the error Playback ID  SMFw_5RXeAYBkMz0 ', '')
	text_str = text_str.replace('http www.samsung.comuksmart switch. People seem to be saying 4 GB. Cnet stream seems to work fine http livestream.comaccounts687825events6034016', '')
	text_str = text_str.replace('http www.pocket lint.comnews138387 ', '')
	text_str = text_str.replace('  http www.slashgear.comchina ', '')
	text_str = text_str.replace('  http www.slashgear.comchina ', '')
	text_str = text_str.replace('http www.theverge.com20166111824118google android', '')
	text_str = text_str.replace('Extended Summaryhttp np.reddit.comrautotldrcomments4m8ik0police_are_filing_warrants_for_androids_vast | FAQhttp np.reddit.comrautotldrcomments31b9fmfaq_autotldr_bot Version 1.6 63745 tldrs so far. | Theoryhttp np.reddit.comrautotldrcomments31bfhttheory_autotldr_concept | Feedbackhttp np.reddit.commessagecompose.to23autotldr PMs and comment replies are read by the bot admin constructive feedback is welcome. | Top keywords  data^1 location^2 Google^3 police^4 users^5 Ugh.. uhhhhhh. Uhhhhhhhhhh.... Rover829https twitter.comRover829 gt2016 03 28 02 03 02 UTChttps twitter.comRover829status714271548102709249gtSamsunghttps twitter.comsearch.q23Samsung says 1 out of 3 who buy a GalaxyS7https twitter.comsearch.q23GalaxyS7 in S.Korea also sign up for phone upgrade program Galaxy Club pic.twitter.comhttp pbs.twimg.commediaCemaEUnWAAAP9p3.jpg ^Imgurhttp i.imgur.comYr7gqXM.jpg    ^Mistake.messagecompose.toTweetPosterampsubjectError20Reportampmessage4cabz10A0APlease leave above link unaltered.^Suggestionmessagecompose.toTweetPosterampsubjectSuggestion^FAQrTweetPostercomments13relk^Codehttps github.comjoealcornTweetPoster^Issueshttps github.comjoealcornTweetPosterissues No extra fees... ', '')
	text_str = text_str.replace('Sourcehttp www.xda developers.comxda external link33 of south korean s7 owners joined the galaxy club upgrade program.', '')
	text_str = text_str.replace('www.theverge.com201622111077956samsung galaxy s7 edge smartphone announced specs mwc 2016 reduced by 88. Im a botgt Itamp039s lower resolution than last yearamp039s 16 megapixel shooter but Samsung says its larger pixels let in 56 percent more light than before for better low light images.gt ', '')
	text_str = text_str.replace('Samsungamp039s business.Extended Summaryhttp np.reddit.comrautotldrcomments46wpzqsamsungs_galaxy_s7_and_s7_edge_bring_refinement | FAQhttp np.reddit.comrautotldrcomments31b9fmfaq_autotldr_bot Version 1.6 38364 tldrs so far. | Theoryhttp np.reddit.comrautotldrcomments31bfhttheory_autotldr_concept | Feedbackhttp np.reddit.commessagecompose.to23autotldr ', '.')
	text_str = text_str.replace(' | Top keywords  Samsung^1 Edge^2 year^3 phone^4 display^5 ', ' ')
	text_str = text_str.replace('amp039s', '')
	text_str = text_str.replace('https www.reddit.comrgadgetscomments5a39o2samsung_galaxy_note_8_confirmed_note_brand_not', '')
	text_str = text_str.replace('https twitter.comJohnLegerestatus785266009422729216 ', '')
	text_str = text_str.replace('\xf0\x9f\x98\x96', '')
	text_str = text_str.replace('https play.google.comstoreappsdetails.idcom.sec.android.app.musicamphlen ', '')
	text_str = text_str.replace(' Source    https twitter.comevleaksstatus749013599239024640 ', '')
	text_str = text_str.replace('https www.reddit.comrGalaxyS6comments3y1fqnhow_do_you_permanently_turn_off_the_app', '')
	text_str = text_str.replace('\xf0\x9f\x98\xa3 Still no confirmation on U3  UHS II MicroSD slot.https www.google.com.ausearch.qu3+uhs2+pins+microsd+fasteramphlenamptbmischampgws_rdcrampei21VzV8z JIym0gSfv57ADw They skipped it to match the s7  Disney. Really.  I got what you needhttps www.reddit.comrsamsungcomments4nbr4dthe_10_companies_millennials_in_the_us_trust_thed43csdm ', '')
	text_str = text_str.replace('https www.reddit.comrsamsungcomments4ctfo6if_your_s7_promotion_estimated_ship_date_shows_as', '')
	text_str = text_str.replace('https www.reddit.comrsamsungcomments4av84fthere_is_native_dpi_scaling_hidden_in_the_galaxyd15d2d4 ', '')
	text_str = text_str.replace('app https play.google.comstoreappsdetails.idde.szalkowski.activitylauncherGo to all activitiesScroll down to settings', '')
	text_str = text_str.replace('https www.reddit.comrAndroidcomments56bjffasus_zenfone_3_zenwatch_3_and_zenpad_3s_10_usd8i4eca', '')
	text_str = text_str.replace('Yuphttp i.imgur.comgiBNDfG.jpg ', '')
	text_str = text_str.replace('\xc2\xa0After totally refusal all my requests i am heartly\xc2\xa0 ask\xc2\xa0 ', '')
	text_str = text_str.replace('\xc2\xa007.14.2015 in the city of Minsk Belarus I bought a cell phone Lenovo Vibe Z2 Pro K920 IMEI 864784020604256.', '')
	text_str = text_str.replace(' http www.androidheadlines.com201505issue', '')
	text_str = text_str.replace('Chinese\xc2\xa0Lenovo and China Mobile', '')
	text_str = text_str.replace('Mikhail Bedniahin', '')
	text_str = text_str.replace('+', '')
	text_str = text_str.replace(' http imgur.comO4zOmyu ^^^ This', '')
	text_str = text_str.replace('Its the T Mobile one. Note 4 N910T Not the same but heres some similar looking ones  1https pp.vk.mec628826v62882604126607Xq9I0tXKpdQ.jpg  2https pp.vk.mec628826v628826041266259q5KUtJiThg.jpg  3https pp.vk.mec622031v62203104136d1983ewf2cSxsI.jpg  4https pp.vk.mec622031v62203104136d208eHUapD1l8Q.jpg  5https pp.vk.mec628826v628826041265f3Yl37618xQ3A.jpg  6https pp.vk.mec622031v62203104136d2fqlvu8Etc0Lk.jpg  7https pp.vk.mec622031v62203104136d28M3HV1diSKwU.jpg  8https pp.vk.mec628826v6288260412661bQZMOVfsbNp4.jpg. ', '')
	text_str = text_str.replace(' Its an S6 activehttp boston.cbslocal.com20160904', '')
	text_str = text_str.replace('\xf0\x9f\x98\xa0', '')
	text_str = text_str.replace('http smile.amazon.comgpoffer listingB012AWBP9Urefolp_twister_child.ieUTF8ampmv_color_name0ampmv_customer_package_type0 Yes it will say it is quick charging if it actually is. I can coil some wires for you for 4 bucks  Massive savings cause larger fires... X Post referenced from rgalaxys7 by usircod  I bought a 14 wireless fast charger on Ebay so you dont have to.https www.reddit.comrGalaxyS7comments4bae97i_bought_a_14_wireless_fast_charger_on_ebay_so    ^^I', '')
	text_str = text_str.replace('\xf0\x9f\x98\x81', '')
	text_str = text_str.replace('CaseyNeistathttps twitter.comCaseyNeistat gt2016 02 26 20 54 43 UTChttps twitter.comCaseyNeistatstatus703322322711789568gtI should not be trusted with all this... thanks SamsungMobileUShttps twitter.comSamsungMobileUS I promise I will try not to screw this up pic.twitter.comhttp pbs.twimg.commediaCcKz4MPW8AAO5S3.jpg ^Imgurhttp i.imgur.comPQowF8B.jpg    ^Mistake.messagecompose.toTweetPosterampsubjectError20Reportampmessage487e920A0APlease leave above link unaltered.^Suggestionmessagecompose.toTweetPosterampsubjectSuggestion^FAQrTweetPostercomments13relk^Codehttps github.combuttsciclesTweetPoster^Issueshttps github.combuttsciclesTweetPosterissues ', '')
	text_str = text_str.replace('https www.reddit.comrSamsungPaycomments46nl1fmilestone_five_million_samsung_pay_users    ^^I ^^am ^^a ^^bot ^^made ^^for ^^your ^^convenience ^^\\Especially ^^for ^^mobile ^^users.  ^^Contacthttps www.reddit.commessagecompose.toOriginalPostSearcher ^^| ^^Codehttps github.compapernotesReddit OriginalPostSearcher ^^| ^^FAQhttps github.compapernotesReddit OriginalPostSearcherfaq ', '')
	text_str = text_str.replace('\xc2\xa350 ', '')
	text_str = text_str.replace('See herehttps www.reddit.comrsamsungcomments4q82kcrumor_note_7_might_have_an_alwayson_back_displayd4r9qf7. I dont know. But edge version   Note http www.sammobile.com20160115samsung patent s pen cover http www.androidauthority.comsamsung patents an s pen case for non note galaxy devices 667834 IP68 with a pen.', '')
	text_str = text_str.replace('http www.samsung.comusmobilecell phones accessoriesEP PG920ABUAT', '')
	text_str = text_str.replace(' https www.frequencycheck.commodelsAk5yrsamsung sm g935f galaxy', '')
	text_str = text_str.replace('http www.amazon.comSamsung Galaxy S7 G935F UnlockeddpB01CJU9BBM However it states that Unlocked cell phones will not work with CDMA Carriers like Sprint Verizon Boost or Virgin  Basically what \xe2\x98\x9d', '')
	text_str = text_str.replace('Heres a screenshot  http imgur.comd5Bffkm X Post referenced from rsamsungpay by ujbus  Korean Galaxy A | Samsung Pay Commercialhttps www.reddit.comrSamsungPaycomments412mo6korean_galaxy_a_samsung_pay_commercial    ^^I ^^am ^^a ^^bot ^^made ^^for ^^your ^^convenience ^^\\Especially ^^for ^^mobile ^^users.  ^^Contacthttps www.reddit.commessagecompose.toOriginalPostSearcher ^^| ^^Codehttps github.compapernotesReddit OriginalPostSearcher ^^| ^^FAQhttps github.compapernotesReddit OriginalPostSearcherfaq ', '')
	text_str = text_str.replace('FTFYhttp lmgtfy.com.qwhattabletshavespen ', '')
	text_str = text_str.replace(' \xf0\x9f\x98\xa2', '')
	text_str = text_str.replace('http www.forbes.comsitesbensin20160912hey samsung do the right thing and open up your note 7 exchange program worldwideamprefURLampreferrer They should have named it Galaxy Explode 7\xe2\x84\xa2.', '')
	text_str = text_str.replace('https www.allstarcardsystems.comshopimagecachedataMAGTEK20USB20CARD20READER202104011020USE 500x500.PNG ', ' ')
	text_str = text_str.replace(' https www.youtube.comwatch.vrNkfjoJQfCY', '')
	text_str = text_str.replace('Please contact the moderators of this subredditmessagecompose.torsamsung if you have any questions or concerns.', '')
	text_str = text_str.replace(' https www.youtube.comwatch.vrNkfjoJQfCY', '')
	text_str = text_str.replace('gt.gt ', '')
	text_str = text_str.replace(' 1 866 553 3239 ', ' ')
	text_str = text_str.replace('The S7S7E is', '')
	text_str = text_str.replace('Nowificouldjustgetittoinsertaspacecorrectlythatwouldbegreatthanks.', '')
	text_str = text_str.replace('https www.youtube.comwatch.v3 61FFoJFy0Watch this.', '')
	text_str = text_str.replace('https youtu.be3 61FFoJFy0 ', '')
	text_str = text_str.replace('https imgur.comwD6oUTK ', '')
	text_str = text_str.replace('push\xe2\x80\x8b out updates. \\^BeccaWell ', '')
	text_str = text_str.replace('\xc2\xa3150 ', '')
	text_str = text_str.replace('   It could be this https www.reddit.comrGalaxyS7comments552pbvbattery_drain_issue_oculus_update_may_be_to_blame it was happening to me this morning.  Uninstalling the Oculus app fixed it immediately You could try this', '.')
	text_str = text_str.replace('\xe2\x80\x98Wipe', '')
	text_str = text_str.replace('X Post referenced from rsamsungpay by ujbus  Samsung Pay adds support for 19 new banks and credit unions xpost rsamsunghttps www.reddit.comrSamsungPaycomments3wy4qrsamsung_pay_adds_support_for_19_new_banks_and    ^^I ^^am ^^a ^^bot ^^made ^^for ^^your ^^convenience ^^\\Especially ^^for ^^mobile ^^users.  ^^Contacthttps www.reddit.commessagecompose.toOriginalPostSearcher ^^| ^^Codehttps github.compapernotesReddit OriginalPostSearcher ', '')
	text_str = text_str.replace('Via   https twitter.comstaguevestatus754962656956735488 ', '')
	text_str = text_str.replace('Acheiva AmegyBank Associated Bank Bayport Credit Union Bethpage California Bank amp Trust Cambridge Savings Bank Financial Center   Your Indiana Credit Union Greater Kinston Credit Union Key Bank KeyPoint Credit Union Navy Federal Credit Union Previously added Numerica Credit Union PenFed PNC PSCU TCFBank USC Credit Union Utah Community Bank Right. ', '')
	text_str = text_str.replace('o_O  ', '')
	text_str = text_str.replace(' 2148374882', '')
	text_str = text_str.replace('Extended Summaryhttp np.reddit.comrautotldrcomments4wwcddsamsung_confirms_galaxy_s7_active_waterproofing | FAQhttp np.reddit.comrautotldrcomments31b9fmfaq_autotldr_bot Version 1.6 88394 tldrs so far. | Theoryhttp np.reddit.comrautotldrcomments31bfhttheory_autotldr_concept | Feedbackhttp np.reddit.commessagecompose.to23autotldr PMs and comment replies are read by the bot admin constructive feedback is welcome. | Top keywords  Samsung^1 Galaxy^2 water^3 Active^4 unit^5 99 ', '')
	text_str = text_str.replace('\xe2\x80\x9ccandidates\xe2\x80\x9d ', '')
	text_str = text_str.replace(' Interestinghttp imgur.com0Kgofm0', '')
	text_str = text_str.replace('  bounce.getresponse.comSigned by  getresponce.com ', '.')
	text_str = text_str.replace('Samsunginsightssea.samsung.com', '')
	text_str = text_str.replace('http imgur.comqZp3UB1 Mmmmmmm ', '')
	text_str = text_str.replace('http www.androidheadlines.com201608samsung ', '.')
	text_str = text_str.replace('\xf0\x9f\x98\x85', '')
	# text_str = text_str.replace('o_O  ', '')
	# text_str = text_str.replace('o_O  ', '')
	return text_str