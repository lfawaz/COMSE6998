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


        val query = "Samsung"

        val tw = new TwitterFactory(cb.build()).getInstance

        val FileName = query + "tweetFile" + Calendar.getInstance.getTime.toString() + ".txt"
        val pw = new PrintWriter(new File(FileName))


        val statuses = tw.search(new Query(query)).getTweets.filter(_.getLang == "en")
        //statuses.foreach(s => println(s.getText))

        //take 20 tweets and produce sentiment score
        val tweets = statuses.take(20).map(Utils.extractText(_)).map(t => (t, SentimentAnalyzer.mainSentiment(t)))
          tweets.foreach(println)
          pw.write(tweets.toString())
          pw.close()




    }
}
