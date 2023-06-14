import Signup from './components/Signup';
import HomeScreen from './components/HomeScreen';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, SafeAreaView, View } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
var Stack = createStackNavigator();

export default function App() {
  return (
<NavigationContainer>
  <Stack.Navigator>
    <Stack.Screen name="Home" component={HomeScreen} />
    <Stack.Screen name="Signup" component={Signup} />
  </Stack.Navigator>
</NavigationContainer>
    );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
