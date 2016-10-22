import com.twStream.Utils.{SentimentAnalyzer, Utils}
import twitter4j.{Query, TwitterFactory, json}
import collection.JavaConversions._
import twitter4j.conf.ConfigurationBuilder


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

        val tw = new TwitterFactory(cb.build()).getInstance
        val statuses = tw.search(new Query("Alleppo")).getTweets
        //statuses.foreach(s => println(s.getText))

        //take 20 tweets and produce sentiment score
        statuses.take(50).map(Utils.extractText(_)).map(t => (t, SentimentAnalyzer.mainSentiment(t))).foreach(println)


    }
}
