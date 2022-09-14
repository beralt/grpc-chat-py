import QtQuick
import QtQuick.Layouts
import QtQuick.Controls as QC

// import our module and use a qualifier
import Alten as A

QC.ApplicationWindow {
    title: "Hello World!"
    width: 400
    height: 200
    visible: true

    GridLayout {
        anchors.fill: parent
        anchors.margins: 8
        columns: 2

        QC.TextField {
            id: name

            Layout.fillWidth: true
            Layout.alignment: Qt.AlignVCenter

            placeholderText: qsTr("Your name")
        }

        QC.Button {
            text: qsTr("Say hello")

            Layout.alignment: Qt.AlignVCenter

            onClicked: function() {
                A.Greeter.greet(name.text)
            }
        }

        Text {
            id: response
            text: A.Greeter.response
        }
    }
}