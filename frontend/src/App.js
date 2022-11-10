import { Box, Button, Center, Flex } from "@chakra-ui/react";
import { useEffect, useState } from "react";
import Plot from "react-plotly.js";

import Table1 from "./Table";

export default function App() {
  const [res, setRes] = useState();
  const [btn, setBtn] = useState(false);
  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/result")
      .then((res) => res.json())
      .then((res) => {
        setRes((state) => res);
        console.log(res);
      });
  }, [btn]);

  return (
    <>
      <Center bg="tomato" p="" w="100%" h="100%" position={"fixed"}>
        <Box bg="white" w="80%" p="10" borderRadius={"md"}>
          <Flex justifyContent={"space-between"}>
            {res && (
              <Plot
                data={[
                  {
                    x: res.valid_func.x,
                    y: res.valid_func.y,
                    name: "истинная функция",
                    type: "scatter",
                    mode: "lines",
                    marker: { color: "red" },
                  },
                  {
                    name: "подогнанная кривая",
                    x: res.aproc_func.x,
                    y: res.aproc_func.y,
                    type: "scatter",
                    mode: "lines",
                  },
                  {
                    x: res.rnd_dots.x,
                    y: res.rnd_dots.y,
                    name: "дискретные данные",
                    type: "scatter",
                    mode: "markers",
                  },
                ]}
                layout={{
                  width: 0.6 * window.innerWidth,
                  title: "Аппроксимация функции",
                  button: "",
                }}
              />
            )}
            <Box>
              <Table1 points={res?.rnd_dots} />
            </Box>
          </Flex>
          <Center>
            <Button
              onClick={() => {
                setBtn((state) => !state);
              }}
            >
              Generate
            </Button>
          </Center>
        </Box>
      </Center>
    </>
  );
}
