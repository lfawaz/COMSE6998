import twitter4j.json

import scala.io.Source
import com.twStream.Utils._


/**
 * Created by szhang206 on 8/15/16.
 * Tweets processing with a saved local JSON file
 */


object twitterTest {
    def main (args: Array[String]): Unit = {

        val tweets = Source.fromFile("sample.20160813-000001.json")
            .getLines()
            .toList
            .filter(x => x.matches("^\\{.*\\}$"))
            .map(json.DataObjectFactory.createStatus)
            .filter(_.getLang == "en" )


        tweets.take(20).map(Utils.extractText(_)).map(t => (t, SentimentAnalyzer.mainSentiment(t))).foreach(println)


    }

}
