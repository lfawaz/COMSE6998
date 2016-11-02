import com.twStream.Utils.{SentimentAnalyzer, Utils}
import twitter4j.{Query, TwitterFactory, json}
import collection.JavaConversions._
import twitter4j.conf.ConfigurationBuilder
import java.io._
import java.util.Calendar
/**
 * Created by szhang206 on 8/31/16.
 */
object twitterAPITest {
    def main (args: Array[String]): Unit = {
        val cb = new ConfigurationBuilder()
        cb.setDebugEnabled(true)
          .setOAuthConsumerKey("2Ona81taJgLn49idswj97JmXg")
          .setOAuthConsumerSecret("8IE99Gr0lCrtbyp0ZZ5KISvF49twPXA6DJLdLukqxUQ8uwhNXt")
          .setOAuthAccessToken("2657538169-EZyrslwb7Pqztaa9NO8V92UfVZpUYsW11TLbj4V")
          .setOAuthAccessTokenSecret("urEAIGHu8ZEnSYUjhejUz6LnL6fCd6MO8VIkObWgDYNN1")

        val YahooFileName = "YahootweetFile" + Calendar.getInstance.getTime.toString() + ".txt"
        val Yahoopw = new PrintWriter(new File(YahooFileName))

        val SamsungFileName = "SamsungtweetFile" + Calendar.getInstance.getTime.toString() + ".txt"
        val Samsungpw = new PrintWriter(new File(SamsungFileName))

        val tw = new TwitterFactory(cb.build()).getInstance
        val Yahoostatuses = tw.search(new Query("Yahoo")).getTweets.filter(_.getLang == "en")
        val Samsungstatuses = tw.search(new Query("Samsung")).getTweets.filter(_.getLang == "en")
        //statuses.foreach(s => println(s.getText))

        //take 20 tweets and produce sentiment score
        val Yahootweets = Yahoostatuses.take(20).map(Utils.extractText(_)).map(t => (t, SentimentAnalyzer.mainSentiment(t)))
        Yahootweets.foreach(println)
        Yahoopw.write(Yahootweets.toString())
        Yahoopw.close()

        val Samsungtweets = Samsungstatuses.take(20).map(Utils.extractText(_)).map(t => (t, SentimentAnalyzer.mainSentiment(t)))
        Samsungtweets.foreach(println)
        Samsungpw.write(Samsungtweets.toString())
        Samsungpw.close()



    }
}
