name := "fetchTweets"

version := "1.0"

scalaVersion := "2.11.8"

libraryDependencies += "org.scala-lang.modules" %% "scala-parser-combinators" % "1.0.4"


libraryDependencies ++= Seq(
  "org.apache.spark" % "spark-core_2.11" % "1.6.2" ,
  "org.apache.spark" % "spark-mllib_2.11" % "1.6.0" ,
  "org.apache.spark" % "spark-streaming_2.11" % "1.6.0",
  "org.apache.spark" % "spark-streaming-twitter_2.11" % "1.6.2",
  "edu.stanford.nlp" % "stanford-corenlp" % "3.6.0",
  "edu.stanford.nlp" % "stanford-corenlp" % "3.6.0" classifier "models",
  "edu.stanford.nlp" % "stanford-parser" % "3.6.0",
  "com.google.protobuf" % "protobuf-java" % "2.6.1",
  "org.twitter4j" % "twitter4j-core" % "4.0.0",
  "org.twitter4j" % "twitter4j-stream" % "4.0.0"


)

