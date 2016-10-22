import com.twStream.Utils.{SentimentAnalyzer, Utils}
import org.apache.spark.streaming.twitter.TwitterUtils
import org.apache.spark.streaming.{Seconds, StreamingContext}
import org.apache.spark.{SparkContext, SparkConf}


/**
 * Created by szhang206 on 8/31/16.
 * Twitter sentiment test with Spark Streaming
 */
object sparkStreamingTest {
    def main (args: Array[String]): Unit = {
        println("Twitter Streaming Test")


        //Setting up SparkConf and SparkContext
        val conf = new SparkConf().setAppName("TestSpark").setMaster("local")
        val sc = new SparkContext(conf)

        //Setting up Spark StreamingContext
        val ssc = new StreamingContext(sc, Seconds(5))


        //Get tweets from stream (optional: filter tweets on keywords)
        //val stream = TwitterUtils.createStream(ssc, None, filters = Array("Hilary", "Trump"))
        val stream = TwitterUtils.createStream(ssc, None)

        //Filter tweets to English only and map it to (Status, Text) tuple
        val statuses = stream.filter(_.getLang == "en" ).map(status => (status, Utils.extractText(status)))

        //statuses.foreach(s => println(s.getText))

        //Extract sentiment from tweets
        //statuses.map(s => SentimentAnalyzer.extractSentiments(s._2)).print()

        //Extract Hashtags and counts
        //val tags = stream.filter(_.getLang == "en" ).flatMap { status => status.getHashtagEntities.map(_.getText)}
        //tags.countByValue().print()



        //ssc.start()
        //ssc.awaitTermination()


    }


}
