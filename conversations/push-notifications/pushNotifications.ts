/* Receiving and handling a push notification */
import {Client, PushNotification} from "@twilio/conversations";

/* push registration. arguments:
 @channelType -  "apn" or "fcm"
 @registrationId - a string, can be retrieved from the firebase
 */
await client.setPushRegistrationId(channelType, registrationId);

// remove push registration
await client.removePushRegistrations(channelType, registrationId);

// handle push notification payload parsing and emit the Client.pushNotification event on this Client instance
await client.handlePushNotification(notificationPayload);

client.on("pushNotification", (pushNotification: PushNotification) => {
    // pushNotification was received by the client
});

// static method for push notification payload parsing
const pushNotification: PushNotification = Client.parsePushNotification(notificationPayload);
