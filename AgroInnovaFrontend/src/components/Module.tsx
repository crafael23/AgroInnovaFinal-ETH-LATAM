import {
	IonButton,
	IonCard,
	IonCardContent,
	IonCardHeader,
	IonCardTitle,
	IonChip,
	IonCol,
	IonItem,
	IonLabel,
	IonToggle,
} from "@ionic/react";
import { useEffect, useState } from "react";

interface Data {
	moduleId: number;
	temperature: number;
	humidity: number;
	valve: boolean;
	client: number;
	id: number;
	dateTime: string;
}

interface User {
	userid: number;
	modules: number[];
}

export function MyComponent(userprops: User) {
	const [data, setData] = useState<Data[]>([]);
	const [error, setError] = useState();
	const [loading, setLoading] = useState(true);

	const [filteredData, setFilteredData] = useState<Data[]>([]);

	const [filteredDataLatest, setFilteredDataLatest] = useState<Data[]>([]);

	const user = userprops;

	useEffect(() => {
		const fetchData = async () => {
			try {
				const response = await fetch(
					"http://bkyz2-fmaaa-aaaaa-qaaaq-cai.localhost:8000/sensorData/get"
				);
				if (response.ok) {
					const jsonData: Data[] = await response.json();
					console.log("jsonData", jsonData);
					const listFilterJsonData: Data[] = [];
					for (let i = 0; i < jsonData.length; i++) {
						if (
							user.modules.includes(jsonData[i].moduleId) &&
							jsonData[i].client === user.userid
						) {
							listFilterJsonData.push(jsonData[i]);
						}
					}

					setFilteredData(listFilterJsonData);
					console.log("listFilterJsonData", listFilterJsonData);
				} else {
					throw error;
				}
			} catch (error) {
				throw error;
			} finally {
				setLoading(false);
			}
		};

		fetchData();

		const intervalId = setInterval(fetchData, 1000); // Fetch data every 4 seconds

		return () => {
			clearInterval(intervalId);
		};
	}, []);

	function removeDuplicates(filteredData: Data[]): Data[] {
		const uniqueData = filteredData.reduce((acc, current) => {
			const existingItem = acc[current.moduleId];
			if (existingItem) {
				if (current.id > existingItem.id) {
					acc[current.moduleId] = current;
				}
			} else {
				acc[current.moduleId] = current;
			}
			return acc;
		}, {} as { [key: number]: Data });

		return Object.values(uniqueData);
	}

	useEffect(() => {
		const dataWithoutDuplicates = removeDuplicates(filteredData);
		setFilteredDataLatest(dataWithoutDuplicates);
	}, [filteredData]);

	if (loading) {
		return <p>Loading...</p>;
	}

	if (error) {
		return <p>Error: {error}</p>;
	}

	return (
		<div>
			{filteredDataLatest.map((item) => (
				<IonCol size="4" key={item.moduleId}>
					<IonCard>
						<IonCardHeader>
							<IonCardTitle className="ion-text-center">
								Modulo {item.moduleId}
							</IonCardTitle>
						</IonCardHeader>
						<IonCardContent>
							<IonItem>
								<IonChip slot="end">{item.humidity}</IonChip>
								<IonLabel slot="start">Humedad</IonLabel>
							</IonItem>
							<IonItem>
								<IonChip slot="end">{item.temperature}</IonChip>
								<IonLabel slot="start">Temperatura</IonLabel>
							</IonItem>
						</IonCardContent>
					</IonCard>
				</IonCol>
			))}
		</div>
	);
}
