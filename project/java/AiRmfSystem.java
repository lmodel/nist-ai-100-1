package example;

/* metamodel_version: 1.12.0 */
/* version: 1.0.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  An engineered or machine-based system that generates outputs such as predictions or decisions for given objectives, with varying autonomy.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AiRmfSystem extends AiRmfRecord {

  private List<String> aiRmfSystemLifecycleStages;


}