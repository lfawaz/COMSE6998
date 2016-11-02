/**
  * Created by lfawaz on 10/4/16.
  */
package com.devdaily.twitterclient
import twitter4j.{Query, Twitter, TwitterFactory}
import twitter4j.conf.ConfigurationBuilder

object ScalaTwitterClientExample {



    // (1) config work to create a twitter object
    val cb = new ConfigurationBuilder()
    cb.setDebugEnabled(true)
      .setOAuthConsumerKey("2Ona81taJgLn49idswj97JmXg")
      .setOAuthConsumerSecret("8IE99Gr0lCrtbyp0ZZ5KISvF49twPXA6DJLdLukqxUQ8uwhNXt")
      .setOAuthAccessToken("2657538169-EZyrslwb7Pqztaa9NO8V92UfVZpUYsW11TLbj4V")
      .setOAuthAccessTokenSecret("urEAIGHu8ZEnSYUjhejUz6LnL6fCd6MO8VIkObWgDYNN1")
    val tf = new TwitterFactory(cb.build())
    val twitter = tf.getInstance()

    for (i <- 1 to 10) {
      val query = new Query("Pepsi")
      val result = twitter.search(query)
      val tweets = result.getTweets().toArray()
      println(tweets(0))
    }



}
