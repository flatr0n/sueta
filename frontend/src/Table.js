import {
  Table,
  Thead,
  Tbody,
  Tr,
  Th,
  Td,
  TableContainer,
} from "@chakra-ui/react";

export default function Table1({ points = { x: [], y: [] } }) {
  return (
    <TableContainer scrollBehavior={"smooth"} overflowY="scroll" h="400">
      <Table variant="simple">
        <Thead>
          <Tr>
            <Th isNumeric>X</Th>
            <Th isNumeric>Y</Th>
          </Tr>
        </Thead>
        <Tbody>
          {points.x.map((x, i) => (
            <Tr key={x}>
              <Td isNumeric>{x}</Td>
              <Td isNumeric>{points.y[i]}</Td>
            </Tr>
          ))}
        </Tbody>
      </Table>
    </TableContainer>
  );
}
