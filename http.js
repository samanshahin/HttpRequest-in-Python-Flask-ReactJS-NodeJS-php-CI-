import React, { useEffect, useState } from 'react';
import { ActivityIndicator, FlatList, Text, View } from 'react-native';

export default function App() {
  const [isLoading, setLoading] = useState(true);
  const [data, setData] = useState([]);
  useEffect(() => {	//or defining TimeOut() to get the updated json file
    fetch('https://reactnative.dev/movies.json')
      .then((response) => response.json())
      .then((json) => setData(json.movies))	//a root field_name in json
      .catch((error) => console.error(error))
      .finally(() => setLoading(false));	//data is loaded (loading is complete now!)
  }, []);
  return (
    <View style={{ flex: 1, padding: 24 }}>
      {isLoading ? <ActivityIndicator /> : (	//if still loading use activityindicator
        <FlatList				//if completed
          data={data}				//get the data
          keyExtractor={({ id }, index) => id}	//default (predefined) structure
          renderItem={({ item }) => (<Text>{item.title}-- {item.releaseYear}</Text>)}	//part of the json
        />
      )}
    </View>
  );
}
