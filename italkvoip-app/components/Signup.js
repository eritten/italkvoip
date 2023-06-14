import {View, Text, TextInput, Button, StyleSheet} from 'react-native';

    function Signup() {
        return (
            <View>
                <Text>Signup</Text>
                <TextInput placeholder="Email" />
                <Tex    tInput placeholder="Password" />
                <TextInput placeholder="Telephone number" />
            <Button title="Signup" />
            </View>
        );
    }

    export default Signup;