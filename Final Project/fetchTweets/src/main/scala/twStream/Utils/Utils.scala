package com.twStream.Utils

/**
 * Created by szhang206 on 8/15/16.
 */
object Utils {
    def extractText(status:twitter4j.Status, removeHashTag:Boolean = true, removeURL:Boolean = true, removeUser:Boolean = true) : String = {

        var raw_text:String = status.getText

        if (removeHashTag) { //Remove HashTags
        val hashTags = status.getHashtagEntities
            for(t <- hashTags) raw_text = raw_text.replaceAll("#" + t.getText, "")
        }



        if (removeUser) { //Remove User Mentions
        val usr = status.getUserMentionEntities
            for(m <- usr) raw_text = raw_text.replaceAll("@" + m.getName + ":?", "")//m.getText
        }


        if (removeURL) { //Remove URLs
            //val urls = status.getURLEntities()
            //for(u <- urls) raw_text = raw_text.replaceAll(u.getURL, "")
            raw_text = raw_text.replaceAll("http[^\\s]*", "")
        }

        raw_text = raw_text.replaceAll("^RT\\s", "").replaceAll("\\n", "")


        raw_text
    }
}
