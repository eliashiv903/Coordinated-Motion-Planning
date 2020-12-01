class Robot:
      def __init__(self, startPlace, currentPlace,endPlace):
            self.startPlace = startPlace
            self.currentPlace = currentPlace
            self.endPlace = endPlace
            # print("Start Place: ", startPlace, "Current Place: ", currentPlace, "End Place: ", endPlace)

      def __str__(self):
            return "Start Place: " + str(self.startPlace) + "Current Place: " + str(self.currentPlace) + "End Place: " + str(self.endPlace)

      def __repr__(self):
            return "Robot"
            # return "Start Place: " + str(self.startPlace) + "     Current Place: " + str(self.currentPlace) + "     End Place: " + str(self.endPlace) + "\n"

