import mwclient
import pandas as pd
from pprint import pprint

site = mwclient.Site('en.wikipedia.org')
pagenames = ['Yahoo!','Criticism_of_Yahoo!','Yahoo!_data_breach',
             'Samsung','Samsung_Electronics','Samsung_Galaxy_Note_7']

for pagename in pagenames:
    page = site.Pages[pagename]
    # Parse all page revisions between 11/19/2015 and 11/19/2016
    revisions = page.revisions(start='2015-11-19T00:00:00Z',
                               end='2016-11-19T23:59:59Z',
                               dir='newer',
                               prop='ids|timestamp|flags|comment|user|content')


    rev_list = []
    while True:
        try:
            rev = revisions.next()
            rev_list.append(rev)
        except StopIteration:
            break

    # Save results to data frame
    rev_df = pd.DataFrame(rev_list)
    rev_file = "wikipedia_edits_"+pagename+".csv"
    rev_df.to_csv(rev_file, encoding='utf-8')
